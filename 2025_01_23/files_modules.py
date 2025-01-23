from pathlib import Path

# Create a Path object
path = Path('/home/user/documents')

# Check if the path exists
print(path.exists())

# Iterate over files in a directory
for file in path.iterdir():
    print(file)
