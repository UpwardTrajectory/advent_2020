import math
from observations import sample, tests, schedules


def parse_sched(data):
    departure, busses = data.split("\n")
    return int(departure), [int(x) if x != 'x' else None for x in busses.split(",")]


def mins_until(bus, t):
    wait_time = bus * (t // bus) + bus - t
    if wait_time == bus:
        return 0
    else:
        return wait_time

    
def find_bus(data):
    my_departure, busses = parse_sched(data)
    wait_times = {bus: mins_until(bus, my_departure) for bus in busses if bus}
    best_bus = sorted(wait_times, key=lambda x: wait_times[x])[0]
    return best_bus * wait_times[best_bus]


def find_cascade(data, start_time=0):
    _, busses = parse_sched(data)
    
    bus_to_offset = [(bus, i) for i, bus in enumerate(busses) if bus]
    synchronized = False
    t = start_time
    d=100
    
    first_bus, others = bus_to_offset[0], bus_to_offset[1:]
    first_bus, _ = first_bus
    t = first_bus * (t // first_bus)
    
    while not synchronized:# and t < 4069781:
       # biggest_t += big_bus
        t += first_bus
        
        if all([offset == mins_until(bus, t) for bus, offset in others]):
            synchronized = True
            print("made it @ ", t)    
                
    if synchronized:
        return t
    raise ValueError("No match found.")
    
    
pred = find_cascade(sample, 0)
assert pred == 1068781, f"we got {pred}"

for ans, data in tests.items():
    pred = find_cascade(data)
    assert pred == ans, f"we got {pred} instead of {ans}"


if __name__ == "__main__":
    print(find_bus(schedules))
    
    