try:
    with open('non_existent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file was not found.")


try:
    with open('protected_file.txt', 'w') as file:
        file.write("Trying to write to a protected file.")
except PermissionError:
    print("You do not have permission to write to this file.")



try:
    with open('some_file.txt', 'r') as file:
        content = file.read()
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred: {e}")



try:
    with open('some_file.txt', 'r') as file:
        content = file.read()
except Exception as e:
    print(f"An unexpected error occurred: {e}")



try:
    with open('some_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("The file was not found.")
finally:
    print("This block is executed no matter what.")
