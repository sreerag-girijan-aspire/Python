class MyClass:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f"MyClass({self.name!r}) representation"
    def __str__(self):
        return f"Name: {self.name}"

obj = MyClass("Alice")
print(repr(obj))  # Output: MyClass('Alice')
print(obj)



class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return MyClass(self.value + other.value)

obj1 = MyClass(10)
obj2 = MyClass(20)
result = obj1 + obj2
print(result.value)  # Output: 30
