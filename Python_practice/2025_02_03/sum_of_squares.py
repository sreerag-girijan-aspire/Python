n=int(input("Enter number of natural numbers "))
sum=0
for i in range(1,n+1):
    sum+=i**2
print(f"Sum of squares {n} natural numbers is {sum}")
