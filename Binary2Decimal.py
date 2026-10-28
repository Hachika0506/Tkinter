binary = input("Enter your Binary: ").strip()
decimal = 0

if binary and all(bit in "01" for bit in binary):
    for bit in binary:
        decimal = decimal * 2 + int(bit)
    print("Decimal : ", decimal)
else:
    print("Please enter only 0s and 1s.")