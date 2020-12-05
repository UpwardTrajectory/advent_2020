from boarding_passes import all_bps

tests = {
    "FBFBBFFRLR": 8*44 + 5,
    "BFFFBBFRRR": 567,
    "FFFBBBFRRR": 119,
    "BBFFBBFRLL": 820
}


def bisect_rows(boarding_pass, lo=0, hi=127, stashed_row=None):
    """Recursively bisect rows & columns until each is isolated to a single value."""
    # Exit Strategy
    if lo == hi: 
        if not boarding_pass:
            return 8 * stashed_row + lo
        if stashed_row is None:
            return bisect_rows(boarding_pass, 0, 7, stashed_row=lo)
    
    # Recursion Logic
    pointer = boarding_pass[0]
    midpt = lo + (hi - lo) // 2
    
    if pointer in "FL":
        return bisect_rows(boarding_pass[1:], lo, midpt, stashed_row)
    if pointer in "BR":
        return bisect_rows(boarding_pass[1:], midpt+1, hi, stashed_row)
    raise ValueError("shouldn't ever get here")    
    

for bp, seat_id in tests.items():
    prediction = bisect_rows(bp)
    assert prediction == seat_id, f"{bp} failed: {prediction} != {seat_id}"
print("All tests passed.")


if __name__ == "__main__":
    
    all_seat_ids = set()
    
    for bp in all_bps.split("\n"):
        all_seat_ids.add(bisect_rows(bp))
    
    biggest = max(all_seat_ids)
    print(biggest)
    
    missing = set(range(biggest)) - all_seat_ids
    my_seat = [x for x in missing if (x+1 in all_seat_ids) & (x-1 in all_seat_ids)]
    print(my_seat)
    