# id()
x = "hello"
print(id(x))  # Returns the unique ID of the object

# type()
print(type(123))  # Returns <class 'int'>

# isinstance()
print(isinstance(123, int))  # Returns True
print(isinstance(123, str))  # Returns False

# issubclass()
class Animal:
    pass

class Dog(Animal):
    pass

print(issubclass(Dog, Animal))  # Returns True
print(issubclass(Animal, Dog))  # Returns False
