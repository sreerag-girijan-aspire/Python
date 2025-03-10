# assert
x = 5
assert x > 0  # No error because condition is True

# gettattr()
class Person:
    name = "Alice"

person = Person()
print(getattr(person, "name"))  # Returns "Alice"

# setattr()
setattr(person, "age", 25)
print(person.age)  # Returns 25

# delattr()
delattr(person, "age")
# print(person.age)  # Raises AttributeError because 'age' is deleted

# hasattr()
print(hasattr(person, "name"))  # Returns True
print(hasattr(person, "age"))  # Returns False
