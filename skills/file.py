import os

def create_file(filename, content=""):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return f"File '{filename}' created."

def read_file(filename):
    if not os.path.exists(filename):
        return f"File '{filename}' does not exist."
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def append_file(filename, content):
    if not os.path.exists(filename):
        return f"File '{filename}' does not exist."
    with open(filename, "a", encoding="utf-8") as f:
        f.write(content)
    return f"Content appended to '{filename}'."

def delete_file(filename):
    if not os.path.exists(filename):
        return f"File '{filename}' does not exist."
    os.remove(filename)
    return f"File '{filename}' deleted."

def rename_file(old_name, new_name):
    if not os.path.exists(old_name):
        return f"File '{old_name}' does not exist."
    os.rename(old_name, new_name)
    return f"File '{old_name}' renamed to '{new_name}'."