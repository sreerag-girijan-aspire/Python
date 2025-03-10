# help()
help(str)  # Displays documentation for the str class

# dir()
print(dir([]))  # Lists attributes of a list

# globals()
print(globals())  # Returns the global symbol table as a dictionary

# locals()
def example():
    a = 10
    print(locals())  # Returns local variables in the function
example()

# callable()
print(callable(len))  # Returns True because len is callable
print(callable(123))  # Returns False because integers are not callable

# isinstance()
print(isinstance("hello", str))  # Returns True


# next()
iter_list = iter([1, 2, 3])
print(next(iter_list))  # Returns 1 (the first item in the iterator)

# memoryview()
data = bytearray(b"hello")
view = memoryview(data)
print(view[0])  # Returns 104 (the ASCII value of 'h')


x = 10
del x  # Deletes the variable x
# print(x)  # Raises NameError because x is deleted


code = 'a = 5\nb = 10\nprint(a + b)'  # Python code as a string
exec(code)  # Executes the code and prints 15
