from questions import all_answers


tests = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def count_any_yes(blob):
    parsed_qs = [x.replace("\n", "") for x in blob.split("\n\n")]
    return sum([len(set(grp)) for grp in parsed_qs])


def count_all_yes(blob):
    parsed_qs = [[set(p) for p in grp.split("\n")] for grp in blob.split("\n\n")]
    return sum([len(set.intersection(*grp)) for grp in parsed_qs])
    

assert count_any_yes(tests) == 11
assert count_all_yes(tests) == 6


if __name__ == "__main__":
    print(count_any_yes(all_answers))
    print(count_all_yes(all_answers))
