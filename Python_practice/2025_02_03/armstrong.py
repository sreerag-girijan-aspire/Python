num=int(input("Enter number to check Armstrong"))
num_copy=num
armstrong=0
while num_copy>0:
    last_digit=num_copy%10
    armstrong+=pow(last_digit,3)
    num_copy//=10
if num==armstrong:
    print("Entered num is Armstrong")
else:
    print("Entered num is not an Armstrong")