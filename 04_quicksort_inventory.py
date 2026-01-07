import time
import random
import sys

# SYSTEM CONFIGURATION
sys.setrecursionlimit(20000) # raises the limit so the program doesn’t crash

def quicksort(array):
    # Base Case: empty list or list with only one element
    if len(array) < 2:
        return array

    else:
        # Pick the middle pivot to avoid worst-case
        mid_index = len(array) // 2
        pivot = array[mid_index]

        # Remove the pivot from the list to avoid infinite loops
        # Then I will create a new list without the pivot element at the index
        items_without_pivot = array[:mid_index] + array[mid_index + 1:] # All items before the pivot + all items after the pivot

        # Divide into less and greater
        less = [i for i in items_without_pivot if i <= pivot]
        greater = [i for i in items_without_pivot if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


# I'll use 100,000 items instead of 1M for this specific demo
# because Python recursion is slow compared to C-based built-ins

data_size = 100000
print(f"Generating inventory of {data_size:,} products...")
# Picking random sample between 1-1000
inventory = [random.randint(0, 1000) for _ in range(data_size)]
# Copy for testing
inventory_native = inventory.copy()

print(f"STARTING SORTING PROTOCOL...")

start_time = time.time()
sorted_inventory = quicksort(inventory)
end_time = time.time()
qs_time = end_time - start_time
print(f"Quicksort: {qs_time:.4f} seconds")



