s = "Hello"
print(len(s))  # Output: 5

s = "hello"
print(s.upper())  # Output: "HELLO"


s = "HELLO"
print(s.lower())  # Output: "hello"


s = "hello"
print(s.capitalize())  # Output: "Hello"


s = "hello world"
print(s.title())  # Output: "Hello World"



s = "  hello  "
print(s.strip())  # Output: "hello"


s = "hello world"
print(s.split())  # Output: ['hello', 'world']


words = ['hello', 'world']
print(' '.join(words))  # Output: "hello world"


s = "hello world"
print(s.replace("world", "there"))  # Output: "hello there"


s = "hello world"
print(s.find("world"))  # Output: 6


s = "hello hello world"
print(s.rfind("hello"))  # Output: 6


s = "hello hello hello"
print(s.count("hello"))  # Output: 3


s = "hello"
print(s.startswith("he"))  # Output: True


s = "hello"
print(s.endswith("lo"))  # Output: True


s = "12345"
print(s.isdigit())  # Output: True


s = "hello"
print(s.isalpha())  # Output: True


s = "hello123"
print(s.isalnum())  # Output: True


s = "hello"
print(s.islower())  # Output: True


s = "HELLO"
print(s.isupper())  # Output: True


s = "Hello World"
print(s.swapcase())  # Output: "hELLO wORLD"


s = "42"
print(s.zfill(5))  # Output: "00042"
