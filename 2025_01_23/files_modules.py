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



import filecmp

# Compare two files
are_files_equal = filecmp.cmp('file1.txt', 'file2.txt')
print(are_files_equal)

# Compare two directories
dir_comparison = filecmp.dircmp('dir1', 'dir2')
dir_comparison.report()
