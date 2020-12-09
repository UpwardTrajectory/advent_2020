from itertools import combinations
import numpy as np
from XMAS_inputs import sample, full_input


def parse_raw(blob):
    return [int(x) for x in blob.split("\n")]


def test_one_weakness(i, data, window):
    possible = data[i-window: i]
    for a, b in combinations(possible, 2):
        if a + b == data[i]:
            return True
    return False
    
    
def find_weakness(data, window):
    for i in range(window, len(data)):
        if not test_one_weakness(i, data, window):
            return data[i]
    return None


def find_rolling_sum(data, target):
    all_sums = list(np.cumsum(data))
    poss_sum_pairs = combinations(all_sums, 2)
    for a, b in poss_sum_pairs:
        if b - a == target:
            min_idx = all_sums.index(a) + 1
            max_idx = all_sums.index(b) + 1
            window = data[min_idx: max_idx]
            return min(window) + max(window)
    return None
            
    
data = parse_raw(sample)
pred = find_weakness(data, 5)
assert pred == 127
assert find_rolling_sum(data, pred) == 62

if __name__ == "__main__":
    data = parse_raw(full_input)
    pred = find_weakness(data, 25)
    
    print(pred)
    print(find_rolling_sum(data, pred))