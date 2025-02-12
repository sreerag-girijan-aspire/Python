n=int(input("Enter num"))
def odd_or_even(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")

@odd_or_even()
def check_valid(n):
    if n.isd:
        return True