# len()
print(len("hello"))  # Returns 5 (length of the string)

# range()
print(list(range(5)))  # Returns [0, 1, 2, 3, 4]

# enumerate()
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)
# Output: 0 a, 1 b, 2 c

# zip()
names = ["Alice", "Bob"]
scores = [90, 85]
print(list(zip(names, scores)))  # Returns [('Alice', 90), ('Bob', 85)]

# all()
print(all([True, True, False]))  # Returns False, since not all are True

# any()
print(any([True, False, False]))  # Returns True, since at least one is True

# filter()
print(list(filter(lambda x: x > 2, [1, 2, 3, 4])))  # Returns [3, 4]

# map()
print(list(map(lambda x: x**2, [1, 2, 3, 4])))  # Returns [1, 4, 9, 16]

# sorted()
print(sorted([3, 1, 4, 2]))  # Returns [1, 2, 3, 4]

# reversed()
print(list(reversed([1, 2, 3])))  # Returns [3, 2, 1]
