print('spam eggs')
print('doesn\'t')  # use \' to escape the single quote...
print("\"Yes,\" they said.")
s = 'First line.\nSecond line.'  # \n means newline
print(s)
print(r'C:\some\name')  # note the r before the quote, you can use raw strings by adding an r before
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""") #String literals can span multiple lines.

word = 'Python'
print(word[0])  # character in position 0
print(word[-1])  # last character
print(word[0:2])
print(word[-2:])  # characters from the second-last (included) to the end
