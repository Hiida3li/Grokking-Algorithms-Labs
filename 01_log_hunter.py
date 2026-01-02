import time

# In a real case, these IDs come from a database
# They are sorted (0, 1, 2, ... 9,999,999)

print("Generating 10 million sorted Log IDs... (Simulating Database Index)")
log_ids = list(range(10000000))

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

# SEARCH (BINARY)
# Open the middle, see 5,000,000
# 7,892,345 is bigger -> Jumps to right half
# Split again -> Finds it instantly

def binary_search(data, target):
    low = 0
    high = len(data) - 1
    steps = 0

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        guess = data[mid]

        if guess == target:
            return steps

        if guess > target:
            high = mid - 1

        else:
            low = mid + 1

    return None

print(f"\n HUNTING FOR TRANSACTION ID: {target_id}")

# Linear
start = time.time()
steps_linear = linear_search(log_ids, target_id)
end = time.time()
print(f" Linear Search: Found in {steps_linear:,} steps | Time: {end - start:.5f} sec") # Linear Search: Found in 7,892,346 steps | Time: 0.21746 sec

# Binary
start = time.time()
steps_binary = binary_search(log_ids, target_id)
end = time.time()
print(f" Binary Search: Found in {steps_binary:,} steps | Time: {end - start:.5f} sec") #  Binary Search: Found in 22 steps | Time: 0.00003 sec

print(f"\n CONCLUSION: To find ID {target_id}, Binary Search saved {steps_linear - steps_binary:,} operations.")
