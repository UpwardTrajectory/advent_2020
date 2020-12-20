from math import prod
import re
from tiles import sample, tiles_and_ids


class Tile(dict):
    ID: int
    up: str
    down: str
    left: str
    right: str
    poss_up: set = set()
    poss_down: set = set()
    poss_left: set = set()
    poss_right: set = set()
        
    @staticmethod
    def build(s):
        s = s.split("\n")
        id_out = int(re.search(" (.*):", s[0]).group(1))
        up_out = s[1]
        down_out = s[-1]
        left_out = ""
        right_out = ""
        
        for row in s[1:]:
            left_out += row[0]
            right_out += row[-1]
            
        final = {
            "ID": id_out,
            "up": up_out,
            "down": down_out,
            "left": left_out,
            "right": right_out
        }
        return Tile(final)
    
    @property
    def all_possible(self):
        possible = set()
        for s in [self['up'], self['down'], self['left'], self['right']]:
            possible.add(s)
            possible.add(s[::-1])
        return possible
    
    @property
    def up_right(self):
        if (len(self['poss_up']) == 0) & (len(self['poss_right']) == 0):
            return True
        return False
    
    @property
    def up_left(self):
        if (len(self['poss_up']) == 0) & (len(self['poss_left']) == 0):
            return True
        return False
    
    @property
    def down_right(self):
        if (len(self['poss_down']) == 0) & (len(self['poss_right']) == 0):
            return True
        return False
    
    @property
    def down_left(self):
        if (len(self['poss_down']) == 0) & (len(self['poss_left']) == 0):
            return True
        return False
    
    @property 
    def is_corner(self):
        if any([self.up_right, self.up_left, self.down_right, self.down_left]):
            return True
        return False
    
        
def solve_puzzle(data):
    tiles = [Tile.build(s) for s in data.split("\n\n")]
    
    for tile in tiles:
        other_tiles = tiles.copy()
        other_tiles.remove(tile)
        tile['poss_up'] = set([t['ID'] for t in other_tiles if tile['down'] in t.all_possible])
        tile['poss_down'] = set([t['ID'] for t in other_tiles if tile['up'] in t.all_possible])
        tile['poss_left'] = set([t['ID'] for t in other_tiles if tile['left'] in t.all_possible])
        tile['poss_right'] = set([t['ID'] for t in other_tiles if tile['right'] in t.all_possible])
           
    return prod([t['ID'] for t in tiles if t.is_corner])



pred = solve_puzzle(sample)
assert pred == 20899048083289
print("Test Passed.")


if __name__ == "__main__":
    print(solve_puzzle(tiles_and_ids))
