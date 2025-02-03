num=int(input("Enter number to check whether it is a Fibonacci "))
prev=0
curr=1
fib=list()
while True:
    next=curr+prev
    fib.append(next)
    prev=curr
    curr=next
    if num<=next:
        break
print(fib)
if num in fib:
    print("Entered number is Fibonacci")
else:
    print("Entered number is not a Fibonacci")

