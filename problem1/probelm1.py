# import files from database.py
from  database import files

pages=0
# def recursive(value):
#     global  pages
#     for key, value in value.items():
#         if isinstance(value, dict):
#             pages+=recursive(value)
#         else:
#             if value is isinstance(value,int):
#                 pages+=value
#         return pages



def calculate_size(dir_path):

    directories = dir_path.split('.')


    current_directory = files


    for directory in directories:
        if directory in current_directory:
            current_directory = current_directory[directory]
        else:
            return f"Directory '{dir_path}' not found."

    total_size = 0

    def recusive(current_directory,total_size):
        if isinstance(current_directory, dict):
            for key, value in current_directory.items():
                if isinstance(value, dict):
                   return recusive(value, total_size)
                else:
                    # print(value)
                    total_size += value

        else:
            return f"Directory '{dir_path}' not found."
        print(total_size,'------------')
        return total_size
    total_size+=recusive(current_directory,total_size)
    return total_size

print(calculate_size("root.dir1.subdir1.subsubdir1.subsubsubdir1"))
print(calculate_size("root.dir1.subdir1.subsubdir1"))
