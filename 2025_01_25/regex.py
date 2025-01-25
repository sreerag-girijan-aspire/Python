import re
m = re.search('(?<=abc)def', 'abcdef')
print(m.group(0))

m = re.search(r'(?<=-)\w+', 'spam-egg')
print(m.group(0))
