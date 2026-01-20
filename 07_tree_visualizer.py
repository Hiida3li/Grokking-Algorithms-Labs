# A dictionary representing a file system, keys are folder/file names
# If the value is a Dictionary, it's a FOLDER, If the value is None, it's a FILE

project_tree = {
    "my_project": {
        "src": {
            "main.py": None,
            "utils": {
                "helpers.py": None,
                "config.py": None
            },
            "models": {
                "user.py": None,
                "product.py": None
            }
        },
        "tests": {
            "test_main.py": None,
            "test_models.py": None
        },
        "README.md": None,
        "requirements.txt": None
    }
}

def print_tree(node, prefix="", is_last=True):
    # This loop handles the dictionary items
    # We convert the dictionary to a list of (key, value) pairs so we can check if it's the last one
    items = list(node.items())
    count = len(items)

    for index, (name, content) in enumerate(items): # name and content = values inside each item
        is_last_item = (index == count - 1) # Checks if this is the last item

        connector = "└── " if is_last_item else "├── "
        # Print the current node
        print(f"{prefix}{connector}{name}")


