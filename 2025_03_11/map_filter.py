numbers = [1, 2, 3, 4, 5]

# Use map with lambda to square each number
squared_numbers = map(lambda x: x * x, numbers)

# Convert map object to a list
print(list(squared_numbers))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Use filter with lambda to get odd numbers
odd_numbers = filter(lambda x: x % 2 != 0, numbers)

# Convert filter object to a list
print(list(odd_numbers))




numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# First, filter out the even numbers, then square the remaining odd numbers
result = map(lambda x: x * x, filter(lambda x: x % 2 != 0, numbers))

# Convert map object to list to see the result
print(list(result))
