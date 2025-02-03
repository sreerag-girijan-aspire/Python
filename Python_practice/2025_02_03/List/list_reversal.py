a = [1, 2, 3, 4, 5]
a.reverse()
print("a=",a)

rev = a[::-1]
print("rev=",rev)
print("a=",a)


rev = list(reversed(a))
print("rev=",rev)