# open()
file = open("example.txt", "w")
file.write("Hello, file!")
file.close()

# read()
file = open("example.txt", "r")
print(file.read())  # Reads and prints the file content
file.close()

# write()
file = open("example.txt", "a")
file.write("\nAppended text")
file.close()

# seek()
file = open("example.txt", "r")
file.seek(0)  # Moves the cursor to the beginning
print(file.read())  # Reads the entire file again
file.close()
