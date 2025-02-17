def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.
    """
    pass

print(my_function.__doc__)
print(my_function())


def add(a, b):
    """Add two numbers and return the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

def subtract(a, b):
    """Subtract two numbers and return the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The difference of the two numbers.
    """
    return a - b

print(add.__doc__)
print(add(3, 4))

print(subtract.__doc__)
print(subtract(10, 5))