def nth_fib(n):
    if n<=0:
        print("Enter num greater than 1")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return nth_fib(n-1)+nth_fib(n-2)
print(nth_fib(5))