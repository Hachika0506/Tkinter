n = int(input("Enter n (try 3 or 5): "))
guess = input("How many times does countdowns call itself for n =" + str(n) + "? ")

input("Recursion - watch each call. Press enter to Run")
def countdown(num):
    print("call - n = ", num)
    if num <= 0:
        countdown(num - 1)
countdown(n)       
print(" calls = ", n + 1,"your guess:", guess, "  ->  O(n)")

input("Watch calls grow with n. Press enter")
for size in range(5, 10):
    print("n = ", size " calls = " size + i, "  ->  O(n)"
          