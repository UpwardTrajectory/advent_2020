import numpy as np
from chairs import sample, waiting_area


def map_area(data):
    return np.array([[np.nan if c == "." else 0 for c in row] for row in data.split("\n")])


def analyze_chairs(m):
    """Iterate through the room & build two lists of indices.
    Use a rolling window to search for empty chairs w/ no-one seated nearby
     -- add to 'going_to_sit'
    Simultainesouly look for filled chairs that ALSO have 4+ neighbors
     -- add to 'going_to_leave'
    
    return (arrive_rows, arrive_cols), (leave_rows, leave_cols)
    which can be used later to slice into 'm'
    """
    arrive_rows, arrive_cols = [], []
    leave_rows, leave_cols = [], []
    col_dim, row_dim = m.shape
    
    for row, one_row in enumerate(m):
        for col, val in enumerate(one_row): 
            r_min = max(0, row-1)
            r_max = min(row_dim, row+2)
            c_min = max(0, col-1)
            c_max = min(col_dim, col+2)
            rolling_window = m[r_min: r_max, c_min: c_max]
            # Will someone sit down?
            if (val == 0) and (np.nansum(rolling_window) == 0):
                arrive_rows.append(row)
                arrive_cols.append(col)
            # Will this chair vacate?  (cutoff @ 5 because of counting self)
            if (val == 1) and (np.nansum(rolling_window) >= 5):
                leave_rows.append(row)
                leave_cols.append(col)
    
    return (arrive_rows, arrive_cols), (leave_rows, leave_cols)


def cycle_once(m):
    """Analyze a seating map (m) and change it in place.
    Return the updated map, and a flag for whether the room is still unstable
    """
    going_to_sit, going_to_leave = analyze_chairs(m)
    
    print(f"Arrived  {len(going_to_sit[0])} | {len(going_to_leave[0])}  Left  |  Current  {int(np.nansum(m))}")
    
    if going_to_sit == going_to_leave:
        print("No changes!  Exiting . . . ")
        return (m, False)
    
    m[going_to_sit] = 1
    m[going_to_leave] = 0   
        
    return (m, True)
   
    
def stabalize_room(data):
    """Parse the raw data, then alternate between filling & vacating
    chairs in the waiting room.
    
    When no more changes can occur, exit the cycle & return the total 
    number of seated visitors.
    """
    m, still_in_flux = map_area(data), True
    
    while still_in_flux:
        m, still_in_flux = cycle_once(m)
    
    return int(np.nansum(m))
        

def show_room(m):
    """Helper function to visualize using original view"""
    view_map = {0: "L", 1:'#'}
    z = np.vectorize(view_map.get)(m)
    z = np.vectorize({"None": ".", "L": "L", "#":'#'}.get)(z)
    z_printout = "\n".join("".join(row) for row in z)
    print(z_printout, "\n")
    return z_printout
    
    
assert stabalize_room(sample) == 37

    
if __name__ == "__main__":
    print(stabalize_room(waiting_area))
    
    
    # Part One bounds: 
    too_high = [2390, 2387]