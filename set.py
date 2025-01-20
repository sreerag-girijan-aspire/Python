basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

a = set('abracadabra')
b = set('alacazam')
print(a - b )                             # letters in a but not in b
print(a | b)                              # letters in a or b or both
print(a & b )                             # letters in both a and b
print(a ^ b)                              # letters in a or b but not both