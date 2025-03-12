def example(*args, **kwargs):
    print(args)  # tuple of positional arguments
    print(kwargs)  # dictionary of keyword arguments

example(1, 2, 3, name="John", age=25)


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof!")
    # pass

dog = Dog()
dog.speak()  # Outputs "Woof!"


def example(*args, **kwargs):
    print(args)  # tuple of positional arguments
    print(kwargs)  # dictionary of keyword arguments

example(1, 2, 3, name="John", age=25)


class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof!")
    # pass

dog = Dog()
dog.speak()  # Outputs "Woof!"


def decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper

@decorator
def greet():
    print("Hello!")

greet()



my_list = ['apple', 'banana', 'cherry']
for idx, item in enumerate(my_list):
    print(idx, item)
