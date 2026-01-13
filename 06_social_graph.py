from collections import deque

# A Hash Map where Key = person, Value =  list of their friends
network = {}

network["you"] = ["bob", "claire", "alice_follower"]
network["bob"] = ["anuj", "peggy"]
network["claire"] = ["thom", "jonny"]
network["alice_follower"] = ["peggy", "alice"] # <--- The connection to the target
network["anuj"] = []
network["peggy"] = []
network["thom"] = []
network["jonny"] = []
network["Alice"] = [] # The target

# Search engine using BFS
def search_connection(start_node, target_name):
    # A Queue to keep track of people to check
    # use 'deque' because it's optimized for adding/removing from both ends
    search_queue = deque()
    search_queue += network[start_node]

    searched = set() # A set to keep track of who already checked
    print(f"Starting search from: {start_node}")
    while search_queue:
        # Pop the first person off the queue
        person = search_queue.popleft()
        if person not in searched: # Check this person if it hasn't checked before
            print(f"  Checking:  {person}")

            if person == target_name:
                print(f"  Found:  {person}")
                return True

            else:
                # If not the target add their friends to the queue
                search_queue += network.get(person, [])
                #Mark as searched
                searched.add(person)

    return False






