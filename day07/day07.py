import re
from math import prod
import networkx as nx
from bag_rules import sample, sample_2, nested_sample, rules


def parse_row(row):
    """For a single rule (row), create acceptable input for nx.build_edges_from()"""
    parent, children = row.split(" bags contain ")
    parsed_children = []
    if children == "no other bags.":
        pass
    else:
        children = children.replace("bags", "").split(", ")
        for child in children:     
            num, adj, color = child.split(" ")[:3]
            name = adj + " " + color
            parsed_children.append((parent, name, {'max_count': int(num)}))

    result = {parent: parsed_children}
   
    return result


def parse_all(text_blob):
    """Iterate over all given rules (text_blob) and build nodes & edges 
    in a format that is acceptable for: 
        nx.add_nodes_from(nodes)
        nx.add_edges_from(edges)
    """
    parsed_rules = {}
    for row in text_blob.split("\n"):
        parsed_rules.update(parse_row(row))
    nodes = set(parsed_rules)
    edges = []
    for grp in parsed_rules.values():
        edges += grp
    
    return nodes, edges


def build_graph(nodes, edges):
    """Create a directed graph between all bag colors
    also contains 'max_count' data
    """
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G    


def count_total_bags_contained_in(bag, G):
    sink_nodes = [node for node, outdegree in G.out_degree(G.nodes()) if outdegree == 0]
    all_paths = [p for sink in sink_nodes for p in nx.all_simple_paths(G, source=bag, target=sink)]
    total = 0
    already_seen = set()
    for path in all_paths:
        for parent, child in zip(path[:-1], path[1:]):
            partial_path = tuple(path[:path.index(child)+1])
            
            if partial_path not in already_seen:
                multipliers = [G.get_edge_data(par, ch)['max_count'] for par, ch in zip(partial_path[:-1], partial_path[1:])]
                total += prod(multipliers)
                already_seen.add(partial_path)       
    return total
        

G1 = build_graph(*parse_all(sample))
G2 = build_graph(*parse_all(sample_2))
G3 = build_graph(*parse_all(nested_sample))

assert len(nx.algorithms.ancestors(G1, 'shiny gold')) == 4

pred = count_total_bags_contained_in('shiny gold', G1)
assert pred == 32, f"{pred} != 32"

pred = count_total_bags_contained_in('shiny gold', G2)
assert pred == 126, f"{pred} != 126"

pred = count_total_bags_contained_in('shiny gold', G3)
assert pred == 35653, f"{pred} != 35653"
                
    
if __name__ == "__main__":
    G = build_graph(*parse_all(rules))
    # Part 1
    print(len(nx.algorithms.ancestors(G, 'shiny gold')))
    # Part 2
    print(count_total_bags_contained_in('shiny gold', G))

