"""
The Scenario: We are building the routing engine for a logistics company.
The Challenge:
Path A (Highway): Direct connection, but heavy traffic (Cost: 10 minutes).
Path B (Side Streets): Requires 3 turns, but no traffic (Cost: 6 minutes total).
BFS would choose Path A (fewer stops). We need Dijkstra to choose Path B (less time).

I Implemented three main data structures:
The Graph: The map of roads and traffic times.
Costs: A table tracking "What is the fastest way to get to Node X so far?"
Parents: A trail of breadcrumbs so we can reconstruct the path at the end.
"""

# Graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6 # Start to A takes 6 minutes
graph["start"]["b"] = 2 # Start to B takes 2 minutes

graph["a"] = {}
graph["a"]["fin"] = 1 # A to Finish takes 1 minute

graph["b"] = {}
graph["b"]["a"] = 3 # B to A takes 3 minutes
graph["b"]["fin"] = 5 # B to Finish takes 5 minutes

graph["fin"] = {} # Finish line has no neighbors


# Costs table: How long does it take to get here from Start?
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Parents table: How did we get here? (To retrace our steps)
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# Processed list: Keep track of nodes we've already calculated
processed = []

