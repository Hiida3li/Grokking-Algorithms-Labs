import time
import random

print("Generating 10,000 songs with random play counts...")

songs = []

for i in range(10000):
    songs.append({
        "id": i,
        "plays": random.randint(1, 100000)


    })

# Make a copy for the "Slow" sort so we don't cheat by sorting the same list twice
selection_sort_copy = songs.copy()
timsort_copy = songs.copy()

# THE Selection Sort WAY
# Finds the max, moves it to the front. Repeats.
# O(n^2)  The "Death Loop"
def selection_sort(data):
    sorted_list = []
    while len(data) > 0:  # I will modify the list, so to loop until it's empty
        max_plays= -1
        max_index= -1

        # Inner Loop: Find the song with the most plays
        for i in range(len(data)):
            if data[i]["plays"] > max_plays:
                max_plays = data[i]["plays"]
                max_index = i
        sorted_list.append(data.pop(max_index))
    return sorted_list


# Uses Timsort (Merge Sort + Insertion Sort combination)
# O(n log n) - Extremely optimized

def python_sort(data):
    return sorted(data, key=lambda x: x["plays"], reverse=True)

print(f"\nSORTING 10,000 SONGS...")
# Result 1: Selection Sort
start_time = time.time()
selection_result = selection_sort(selection_sort_copy)
end_time = time.time()
time_for_selection= end_time - start_time

print(f"Selection Sort (Junior): {time_for_selection:.4f} seconds")

# Result 2: Python Sort
start_time = time.time()
timsort_result = python_sort(timsort_copy)
end_time = time.time()
time_for_timsort = end_time - start_time
print(f"Python Native Sort (Senior): {time_for_timsort:.6f} seconds")

if time_for_selection > 0 and time_for_timsort > 0:
    speedup = time_for_selection / time_for_timsort
    print(f"\nEFFICIENCY GAIN: Native Sort is {speedup:.0f}x Faster")

