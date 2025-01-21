class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
    
print(MyClass.i)
print(MyClass.f(0))



class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
print(d.name,d.kind)


class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Buddy')
d.add_trick('roll over')
print(d.tricks)