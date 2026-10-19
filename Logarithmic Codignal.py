n = 10

guess = input("Double loop at n - 10 checks n * n pairs. How many pairs? ")

input("Formula: one calculation, done. Press Enter to run")
steps = 1
print(" steps =", steps, " -> O(1) constant time -> steps never change")

input("Loop: one step per item. Press Enter to run")
steps = 0
for i in range(n):
    for j in range(n):
        steps += 1
print(" steps =", steps, " your guess:", guess, " -> O(n^2) quadratic time -> steps")

input("Two more notations. Press Enter to run")
print("Big Omega O  -> best case lower bound")
print("Big Theta O  -> exact bound (worst = best)")
