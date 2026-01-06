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

