input("XOR with 0 keeps the number,Press Enter")
print(" 5^ 0 = "^,5^0)
print(" 9 ^ 9 = "^,9^9)

input("XOR with itself gives 0,Press Enter")
print(" 5^ 5 = "^,5^5)
print(" 9 ^ 9 = "^,9^9)

n = int(input("Enter a number (try 6 or 11): "))
guess = input("what is 3 ^ " + str(n) + " ^ 3 ? ")
input("XOR cancels - 3 appears twice so it dissappears. Press Enter")
print("3 ^ ",n," ^ 3 = ",3^n^3,"your guess:",guess)
