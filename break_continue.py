for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break


for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

    # Example with break
    for num in range(10, 20):
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} equals {i} * {num//i}")
                break
        else:
            # loop fell through without finding a factor
            print(f"{num} is a prime number")

    # Example with continue
    for num in range(10, 20):
        if num % 2 == 0:
            print(f"Skipping even number {num}")
            continue
        for i in range(3, num, 2):
            if num % i == 0:
                print(f"{num} equals {i} * {num//i}")
                break
        else:
            # loop fell through without finding a factor
            print(f"{num} is a prime number")