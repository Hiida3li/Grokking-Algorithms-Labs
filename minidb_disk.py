import os
import struct

# CONSTANTS
PAGE_SIZE = 4096  # 4KB standard page size


class DiskManager:
    def __init__(self, filename="my_database.db"):
        self.filename = filename
        self.file = open(self.filename, "r+b") if os.path.exists(self.filename) else open(self.filename, "w+b")

    def _seek(self, page_id):
        """Moves the file cursor to the correct spot for a specific Page ID."""
        offset = page_id * PAGE_SIZE
        self.file.seek(offset)

    def write_page(self, page_id, data):
            """
            Saves a 4KB chunk of data to the disk at location page_id.
            """
            if len(data) > PAGE_SIZE:
                raise ValueError(f"Data too large! Max {PAGE_SIZE} bytes.")
            self._seek(page_id)
            # Pad the data with null bytes if it's smaller than 4KB
            padded_data = data.ljust(PAGE_SIZE, b'\x00')
            self.file.write(padded_data)
            self.file.flush() # Force the OS to write to disk immediately

    def read_page(self, page_id):
        """
        Reads a 4KB chunk of data from the disk at location page_id.
        """
        self._seek(page_id)
        data = self.file.read(PAGE_SIZE)
        return data

    def close(self):
        self.file.close()

if __name__ == "__main__":
    print("INITIALIZING DISK MANAGER...")
    db = DiskManager()

# Create some dummy data
    print(" Writing Page 0 (Metadata)...")
    header_info = b"Header: Root_ID=5"
    db.write_page(0, header_info)

    print("Writing Page 5 (User Data)...")
    user_data = b"User: Mahmoud | Role: Engineer | Status: Active"
    db.write_page(5, user_data)

    db.close()
    print("Database Closed.")

    # Re-open to prove persistence
    print("\n Re-opening Database...")
    db_new = DiskManager()

    page_0 = db_new.read_page(0)
    page_5 = db_new.read_page(5)

# Show first 20-bytes
    print(f"Read Page 0: {page_0[:20]}")
    # Show first 50-bytes
    print(f"Read Page 5: {page_5[:50]}")



# Clean up (delete the file so we can run it again later)
    db_new.close()

    # Uncomment to delete after test
    # os.remove("my_database.db")
