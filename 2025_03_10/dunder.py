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


class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __len__(self):
        return len(self.value)

obj = MyClass([1, 2, 3])
print(len(obj))  # Output: 3

class MyClass:
    def __init__(self, items):
        self.items = items
    
    def __getitem__(self, index):
        return self.items[index]

obj = MyClass([1, 2, 3])
print(obj[1])  # Output: 2


class MyClass:
    def __init__(self, items):
        self.items = items
    
    def __setitem__(self, index, value):
        self.items[index] = value

obj = MyClass([1, 2, 3])
obj[1] = 5
print(obj.items)  # Output: [1, 5, 3]

class MyClass:
    def __del__(self):
        print("Object is being deleted")

obj = MyClass()
del obj  # Output: Object is being deleted


class MyClass:
    def __init__(self, value):
        self.value = value
    
    def __call__(self):
        return f"Called with value {self.value}"

obj = MyClass(10)
print(obj())  # Output: Called with value 10



class MyClass:
    def __init__(self, items):
        self.items = items
    
    def __iter__(self):
        return iter(self.items)

obj = MyClass([1, 2, 3])
for item in obj:
    print(item)
# Output:
# 1
# 2
# 3



class MyClass:
    def __init__(self, items):
        self.items = items
    
    def __contains__(self, item):
        return item in self.items

obj = MyClass([1, 2, 3])
print(2 in obj)  # Output: True
