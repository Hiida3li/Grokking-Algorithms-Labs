
# Using {} (Set Literal) is faster than set([])
states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}

# Each station covers a specific region
stations = {}
stations["kone"] = {"id", "nv", "ut"}
stations["ktwo"] = {"wa", "id", "mt"}
stations["kthree"] = {"or", "nv", "ca"}
stations["kfour"] = {"nv", "ut"}
stations["kfive"] = {"ca", "az"}

final_stations = set()
print(f"TARGET: Cover {len(states_needed)} states with minimum stations")

# Loop until we have covered every single state
while states_needed:
    best_station = None
    states_covered = set()

    # Check every station to see which one covers the most uncovered states
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station

        # If this station covers more than the current best, it becomes the new best
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    # If we found a station add it to our cart
    if best_station:
        final_stations.add(best_station)
        # DIFFERENCE (-): Remove the covered states from the 'needed' list
        states_needed -= states_covered
        print(f"   Picked '{best_station}' (Covers {len(states_covered)} new states)")
        print(f"   Remaining states needed: {len(states_needed)}")
