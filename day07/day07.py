import re
from bag_rules import sample, rules


def parse_row(row):
    
    try:
        parent, children = row.split(" bags contain ")
        if children == "no other bags.":
            parsed_children = {}
        else:
            parsed_children = {}
            children = children.replace("bags", "").split(", ")
            for child in children:     
                num, adj, color = child.split(" ")[:3]
                name = adj + " " + color
                parsed_children[name] = int(num)
                
        result = {parent: parsed_children}
    except Exception as e:
        result = "exception"
        print(e)
    return result


def parse_all(blob):
    all_rules = {}
    for row in blob.split("\n"):
        all_rules.update(parse_row(row))
    return all_rules


def count_valid_outermost(target, bag_rules):
    total = 0
    for bag, rules in bag_rules.items():
        if target in rules:
            total += 1
            
                
    
parse_all(sample)
