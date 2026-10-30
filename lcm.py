num1 = int(input("Enter First Number"))
num2 = int(input("Enter Second Number"))

a = num1
b = num2

i = 2
lcm = 1

while a > i or b > i:
    if a % i == 0 or b % i == 0:
        lcm = lcm * i

        if a % i == 0:
            a = a // i

        if b % i == 0:
            b = b // i
    else:
        i = i + 1
print("LCM =", lcm)                    