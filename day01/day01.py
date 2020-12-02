import numpy as np
import itertools


with open('inputs.txt', 'r') as f:
    expense_report = f.read()
    
expense_report = [float(x) for x in expense_report.split('\n')]


def get_result(expense_reports, tally=2020, in_operation=np.sum, out_operation=np.prod):
    """Given expense_reports: a list of input lists
    get all permutations of possible combos
    use in_operation() : must operate on an array
    to find the tally : something that in_operation can yield
    then return the out_operation() on the successful combo
    """
    possible = itertools.product(*expense_reports)

    for group in possible:
        if in_operation(group) == tally:
            #print(group)
            return int(out_operation(group))
    return None


if __name__ == "__main__":
    
    for n in [2, 3]:
        poss_combos = [expense_report] * n
        print(get_result(poss_combos))
    
        
    