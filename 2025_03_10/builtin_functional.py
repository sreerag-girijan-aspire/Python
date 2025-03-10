# lambda()
add = lambda x, y: x + y
print(add(3, 4))  # Returns 7

# reduce() (requires functools)
from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))  # Returns 10 (sum of list elements)
