from pathlib import Path

# Create a Path object
path = Path('/home/user/documents')

# Check if the path exists
print(path.exists())

# Iterate over files in a directory
for file in path.iterdir():
    print(file)



import os

# Get the absolute path
abs_path = os.path.abspath('example.txt')
print(abs_path)

# Check if a path is a file
is_file = os.path.isfile('example.txt')
print(is_file)
