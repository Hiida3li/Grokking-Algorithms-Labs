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
            self.file.flush()
