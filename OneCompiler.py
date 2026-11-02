from math import sqrt
num = int(input("Enter a number: "))

for k in range(2, int(sqrt(num)) + 1):
    if num % k == 0:
        print(f"{num} is not a prime number")
        break
else:
    print(f"{num} is a prime number")