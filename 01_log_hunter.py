import time

# In a real case, these IDs come from a database
# They are sorted (0, 1, 2, ... 9,999,999)

print("Generating 10 million sorted Log IDs... (Simulating Database Index)")
log_ids = list(range(1000000))

# The scenario says: "My transaction 7892345 failed!"
# We need to find this specific ID in the pile to check the logs
target_id = 7892345

# SEARCH (Linear)
def linear_search(data, target):
    steps = 0
    for item in data:
        steps +=1
        if item == target:
            return steps
    return None


