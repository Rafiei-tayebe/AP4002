# importing os module
import os

# Get the current working
# directory (CWD)
cwd = os.getcwd()

# Print the current working
# directory (CWD)
print("Current working directory:", cwd)

# Get the list of all files and directories
# in the root directory
path = cwd
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# print the list
print(dir_list)

# join a Leaf directory to the parent directory
directory = "images"

# Parent Directories
parent_dir = cwd

# os.path.join
path = os.path.join(parent_dir, directory)
print(f'Joining {parent_dir} and {directory}')
print(path)

# os.path.isdir
for file in dir_list:
    print(f'{file} is a directory: {os.path.isdir(file)}')

# https://www.geeksforgeeks.org/os-module-python-examples/
