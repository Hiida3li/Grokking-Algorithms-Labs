import time

# Caching is simply a Python Dictionary-Hash Map
# Key: The URL (e.g., "google.com")
# Value: The Data (e.g., "<html>...</html>")

cache = {}

# SLOW DATABASE SIMULATION
def get_data_from_database(url):
    print("Connecting to database for: {url}...")
    # Simulate a slow network request or heavy SQL query
    time.sleep(2)
    return f"DATA_FOR_{url.upper()}"

# The CACHE PROXY
def fetch_page(url):
    # Check the Hash Map
    if url in cache:
        print(f"CACHE HIT: Found {url} in memory!")
        return cache[url]
    else:
        print(f"CACHE MISS: {url} not found. Fetching from database...")
        data = get_data_from_database(url)

        # Save it in Caching
        cache[url] = data
        return data

requests = ["facebook.com", "facebook.com", "facebook.com", "google.com", "facebook.com"]

print("SERVER STARTING...")

for req in requests:
    print(f"\nRequesting: {req}")
    start = time.time()

    response = fetch_page(req)
    end = time.time()
    print(f"Time Taken: {end - start:.4f} seconds")

print("\nANALYSIS: Notice the first request took 2s. The rest took 0s")







