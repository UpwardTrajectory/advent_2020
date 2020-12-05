from boarding_passes import all_bps


tests = {
    "FBFBBFFRLR": 8*44 + 5,
    "BFFFBBFRRR": 567,
    "FFFBBBFRRR": 119,
    "BBFFBBFRLL": 820
}


def bisect_values(boarding_pass, lo=0, hi=127, stashed_row=None):
    """Recursively bisect rows & columns until each is isolated to a single value."""
    # Exit Strategy
    if lo == hi: 
        if not boarding_pass:
            return 8 * stashed_row + lo
        if stashed_row is None:
            return bisect_values(boarding_pass, 0, 7, stashed_row=lo)
    
    # Recursion Logic
    pointer = boarding_pass[0]
    midpt = (lo + hi) // 2
    
    if pointer in "FL":
        return bisect_values(boarding_pass[1:], lo, midpt, stashed_row)
    if pointer in "BR":
        return bisect_values(boarding_pass[1:], midpt+1, hi, stashed_row)
    raise ValueError("shouldn't ever get here")    
    

for bp, seat_id in tests.items():
    prediction = bisect_values(bp)
    assert prediction == seat_id, f"{bp} failed: {prediction} != {seat_id}"
print("All tests passed.")


if __name__ == "__main__":
    
    all_seat_ids = set(bisect_values(bp) for bp in all_bps.split("\n"))

    biggest = max(all_seat_ids)    
    empty_seats = set(range(min(all_seat_ids), biggest)) - all_seat_ids
    
    print(f"Biggest: {biggest}\nMy Seat: {empty_seats.pop()}")
    