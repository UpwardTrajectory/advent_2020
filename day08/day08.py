from instructions import sample, startup_code


ALL_OPPS = {
    ###           x = (num, pointer)
    'nop': lambda x: nop(*x)
    , 'jmp': lambda x: jmp(*x)
    , 'acc': lambda x: acc(*x)
}


def nop(num, pointer):
    pointer['cur_line'] += 1
    return pointer


def jmp(num, pointer):
    pointer['cur_line'] += num
    return pointer


def acc(num, pointer):
    pointer['cur_line'] += 1
    pointer['accumulator'] += num
    return pointer


def parse_code(text_blob):
    get_code_from_idx = []
    for row in text_blob.split("\n"):
        code, num = row.split(" ")
        get_code_from_idx.append((code, int(num)))
    return get_code_from_idx


def find_repeated_line(get_code_from_idx):
    seen = set()
    pointer = {'cur_line': 0, 'accumulator': 0}
    
    while True:
        cur_line = pointer['cur_line']
        # Exit Strategy P2:  transfer "WIN" condition via datatype == string
        if cur_line >= len(get_code_from_idx):
            return str(pointer['accumulator'])
        # Exit Strategy P1: if beginning an infinite loop, exit w/ accumulator total instead
        if (cur_line in seen):
            return pointer['accumulator']
        seen.add(cur_line)
        process_line(pointer, get_code_from_idx[cur_line])

    
def process_line(pointer, single_code, all_opps=ALL_OPPS):
    """Process a single line of code, return updated 'pointer'"""
    opp, num = single_code    
    all_opps[opp]((num, pointer))
    return pointer


def test_all_jmp_nop(get_code_from_idx):
    needs_checking = [i for i, x in enumerate(get_code_from_idx) if x[0] in {'jmp', 'nop'}]
    seen = set()
    replace_cmd = {'jmp': 'nop', 'nop': 'jmp'}
    
    for idx in needs_checking:
        bad_cmd, num = get_code_from_idx[idx]
        new_codes = get_code_from_idx.copy()
        new_codes[idx] = replace_cmd[bad_cmd], num
        accumulated = find_repeated_line(new_codes)
        # Early exit if "WIN" condition found 
        if isinstance(accumulated, str):
            return int(accumulated)
        seen.add((idx, accumulated))
    
    return seen
    

get_code_from_idx = parse_code(sample)
pred = find_repeated_line(get_code_from_idx)
assert pred == 5, f"sample failed. {pred} != 5"


if __name__ == "__main__":
    get_code_from_idx = parse_code(startup_code)

    print(find_repeated_line(get_code_from_idx))
    print(test_all_jmp_nop(get_code_from_idx))
    