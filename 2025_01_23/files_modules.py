from pathlib import Path

# Create a Path object
path = Path.cwd()

# Check if the path exists
print(path.exists())

# Iterate over files in a directory
for file in path.iterdir():
    print(file)


print()
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

# # Compare two directories
# dir_comparison = filecmp.dircmp('dir1', 'dir2')
# dir_comparison.report()




import tempfile

# Create a temporary file
with tempfile.TemporaryFile() as temp_file:
    temp_file.write(b'Hello, World!')
    temp_file.seek(0)
    print(temp_file.read())




import glob

# Find all .txt files in the current directory
txt_files = glob.glob('*.txt')
print(txt_files)



import fnmatch
import os

# List all .txt files in the current directory
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.txt'):
        print(file)



import linecache

# Get a specific line from a file
line = linecache.getline('file1.txt', 3)
print(line)


import shutil

# Copy a file
shutil.copy('source.txt', 'destination.txt')

# Archive a directory
shutil.make_archive('archive_name', 'zip')
