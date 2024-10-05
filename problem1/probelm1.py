# import files from database.py
from  database import files

def calculate_size(dir_path):

    directories = dir_path.split('.')


    current_directory = files


    for directory in directories:
        if directory in current_directory:
            current_directory = current_directory[directory]
        else:
            return f"Directory '{dir_path}' not found."


    total_size = 0


    if isinstance(current_directory, dict):
        for key, value in current_directory.items():
            if isinstance(value, dict):
                continue
            total_size += value
    else:
        return f"Directory '{dir_path}' not found."

    return total_size



print(calculate_size(files,"root.dir1.subdir1"))