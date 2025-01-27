import re
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m.group(0))       # The entire match
print(m.group(1))       # The first parenthesized subgroup.
print(m.group(2))       # The second parenthesized subgroup.
print(m.group(1, 2) )
print(m.groups())




# Check if the string starts with 'Hello'
pattern = r'^Hello'
string = 'Hello, world!'
match = re.match(pattern, string)
print(match)  # Output: True



# Find all occurrences of 'cat' in the string
pattern = r'cat'
string = 'The cat sat on the cat mat.'
matches = re.findall(pattern, string)
print(matches)  # Output: ['cat', 'cat']




# Replace all digits with '#'
pattern = r'\d'
string = 'My phone number is 123-456-7890.'
new_string = re.sub(pattern, '#', string)
print(new_string)  # Output: 'My phone number is ###-###-####.'



# Split the string by spaces
pattern = r'\s+'
string = 'Split this string by spaces.'
parts = re.split(pattern, string)
print(parts)  # Output: ['Split', 'this', 'string', 'by', 'spaces.']




# Find all words starting with 's'
pattern = r'\bs\w*'
string = 'She sells sea shells by the sea shore.'
matches = re.findall(pattern, string)
print(matches)  # Output: ['She', 'sells', 'sea', 'shells', 'sea', 'shore']
