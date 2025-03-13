x = 10  # Integer
y = 3.14  # Float
name = "Alice"  # String
is_student = True  # Boolean

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  

coordinates = (10, 20)
print(coordinates[1]) 

person = {"name": "Alice", "age": 25}
print(person["name"])  

if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")

for fruit in fruits:
    print(fruit)

count = 0
while count < 5:
    print(count)
    count += 1

def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"

my_dog = Dog("Buddy", 3)
print(my_dog.bark())

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

with open("example.txt", "w") as file:
    file.write("Hello, world!")

with open("example.txt", "r") as file:
    content = file.read()
    print(content)