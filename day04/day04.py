from passports import sample, valid, invalid, batched_passports
import re


def parse_multiple(passports):
    """Convert text blob into list of dictionaries
    No validation is performed in this step
    """
    as_strings = [row.replace(" ", ",").replace("\n", ",") for row in passports.split("\n\n")]
    
    parsed_passports = []
    for passport in as_strings:
        parsed_pp = {}
        for attribute in passport.split(","):
            k, v = attribute.split(":")
            parsed_pp[k] = v
        parsed_passports.append(parsed_pp)
    return parsed_passports


def validate_one(pp):
    """byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    try:
        byr = float(pp['byr'])
        iyr = float(pp['iyr'])
        eyr = float(pp['eyr'])
        hgt = pp['hgt']
        hcl = pp['hcl']
        ecl = pp['ecl']
        pid = pp['pid']
          
        all_necessary_attributes = {
            # Decimal years (ie. 1982.5) are not allowed
            'byr': (byr == int(byr)) & (1919 < byr < 2003),
            'iyr': (iyr == int(iyr)) & (2009 < iyr < 2021),
            'eyr': (eyr == int(eyr)) & (2019 < eyr < 2031),
            'hgt': check_height(hgt),
            'hcl': bool(re.search(r'^#(?:[0-9a-f]{3}){1,2}$', hcl)),
            'ecl': ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'),
            'pid': bool(re.search(r'^\s*(?:[0-9]{9})\s*$', pid)),        
        }
        return True if sum(all_necessary_attributes.values()) == 7 else False
    except KeyError:
        return False
    except Exception as e:
        print(e)
        return False
    

def check_height(hgt):
    """hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    """
    num, unit = hgt[:-2], hgt[-2:]
    
    if unit == 'cm' and (150 <= float(num) <= 193):
        return True
    if unit == 'in' and (59 <= float(num) <= 76):
        return True
    return False


# def validate_keys(parsed_pp):
#     """DEPRECIATED
#     Ensure 7 essential keys are in a passport.
#     'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'
#     """
#     status = False
#     necessary_keys = set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'])
#     current_keys = set(parsed_pp.keys())
#     current_keys.discard('cid')
#     return current_keys == necessary_keys


def count_valid_from_batch(passports):
    return sum(validate_one(pp) for pp in parse_multiple(passports))


assert count_valid_from_batch(sample) == 2, f'sample failed: 2 vs {count_valid_from_batch(sample)}'
assert count_valid_from_batch(invalid) == 0, 'invalid failed'
assert count_valid_from_batch(valid) == 4, f'valid failed: 4 vs {count_valid_from_batch(valid)}'


if __name__ == "__main__":
    print(count_valid_from_batch(batched_passports))