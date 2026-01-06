import time

# SIMULATION (A Deeply Nested File System)
# This dictionary represents folders inside folders
# "files" is a list of files in that folder
# "subfolders" is a dictionary of more folders

mock_file_system = {
    "root": {
        "files": ["readme.txt", "logo.png"],
        "subfolders": {
            "users": {
                "files": ["user_list.csv"],
                "subfolders": {
                    "admin": {
                        "files": ["config.yaml"],
                        "subfolders": {
                            "hidden": {
                                "files": ["passwords.txt", "keys.pem"],  # <--- TARGET
                                "subfolders": {}
                            }
                        }
                    },
                    "guest": {
                        "files": ["pic.jpg"],
                        "subfolders": {}
                    }
                }
            },
            "logs": {
                "files": ["error.log", "access.log"],
                "subfolders": {}
            }
        }
    }
}

def search_filesystem(current_folder, path_so_far, target_filename):
    print(f"Scanning: {path_so_far}...")

    # BASE CASE (The Stop Condition)
    if target_filename in current_folder["files"]:
        return f"{path_so_far}/{target_filename}" # If yes returns the full path

    # If there are subfolders, dive into them
    for folder_name, subfolder_data in current_folder["subfolders"].items():
        new_path = f"{path_so_far}/{folder_name}"
        result = search_filesystem(subfolder_data, new_path, target_filename)
        if result:
            return result

    return None


target = "passwords.txt"
print(f"STARTING CRAWL FOR: {target}")

start = time.time()
found_path = search_filesystem(mock_file_system["root"], "/root", target)
end = time.time()


if found_path:
    print(f"\nTARGET ACQUIRED")
    print(f"Location: {found_path}")
    print(f"Time: {end - start:.4f} sec")

else:
    print(f"\nTARGET NOT FOUND")


