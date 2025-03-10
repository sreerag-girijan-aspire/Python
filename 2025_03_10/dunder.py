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
