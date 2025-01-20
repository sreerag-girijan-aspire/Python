squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[-1])

print(squares + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)

rgb = ["Red", "Green", "Blue"]
rgba = rgb
rgba.append("Alph")
print(rgb)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = [] # remove the letters from index 2 to 5
print(letters)


letters[:] = [] # clear the list by replacing all the elements with an empty list
print(letters)

print(len(letters))

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)


# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b


a, b = 0, 1
while a < 1000:
    print(a, end=',') # One line print
    a, b = b, a+b