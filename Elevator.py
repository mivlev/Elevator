import argparse

# Global variable for single floor travel time
single_floor_travel_time = 10


# Function that calculates total travel time given an ordered list of floors to visit
def calc_travel_time(floor_order: list[int]) -> None:
    travel_time = 0

    # Iterates through list of floors to visit and calculates travel time between each pair of floors
    for i in range(len(floor_order) - 1):
        travel_time += abs(floor_order[i] - floor_order[i + 1]) * single_floor_travel_time

    print(f"Travel time: {travel_time}\nOrder of floors visited: {floor_order}")

    return


# Function that calculates the order in which floors will be visited
# Takes a boolean "direction" that indicates the direction that the elevator moves first,
# as well as the sorted list of floors to visit and the starting floor
def calc_floor_order(direction: bool, start: int, floors_to_visit_sorted: list[int]) -> None:

    # Get index of start floor
    start_floor_idx = floors_to_visit_sorted.index(start)

    # Elevator moves down first
    if direction:
        # All floors to visit below starting floor in descending order, then floors above in ascending order
        floor_order = floors_to_visit_sorted[0:start_floor_idx + 1][::-1]
        floor_order.extend(floors_to_visit_sorted[start_floor_idx + 1:len(floors_to_visit_sorted)])

    # Elevator moves up first
    else:
        # All floors to visit above starting floor in ascending order, then floors below in descending order
        floor_order = floors_to_visit_sorted[start_floor_idx:len(floors_to_visit_sorted)]
        floor_order.extend(floors_to_visit_sorted[0:start_floor_idx][::-1])

    # Calls final helper function
    calc_travel_time(floor_order)

    return


def elevator(start: int, floors_to_visit: list[int]) -> None:

    # Adds starting floor to list of floors to visit
    if start not in floors_to_visit:
        floors_to_visit.append(start)

    # Sorts the user inputted list of floors that need to be visited
    floors_to_visit = sorted(floors_to_visit)

    # Calculates the distance above and below starting floor that the elevator must travel
    # The elevator should first move in the direction of the shorter distance
    dist_down = start - min(floors_to_visit)
    dist_up = max(floors_to_visit) - start

    # Calls to first helper function
    if dist_down < dist_up or dist_down == dist_up:
        calc_floor_order(True, start, floors_to_visit)
    else:
        calc_floor_order(False, start, floors_to_visit)

    return


if __name__ == "__main__":

    # Parses command line arguments passed in by the user
    parser = argparse.ArgumentParser(description="Simulation of an elevator")
    parser.add_argument("start", type=int, help="The floor that the elevator starts on. Example: 3")
    parser.add_argument("floors_to_visit", type=str, help="List of floors that the elevator needs to visit. Example: 1,2,3,4")
    args = parser.parse_args()

    floors_to_visit = args.floors_to_visit.split(',')

    # Invalid input handling
    try:
        elevator(args.start, [int(x) for x in floors_to_visit])
    except:
        print("Invalid input. Please run the following command for help: python elevator.py -h")