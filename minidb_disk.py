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