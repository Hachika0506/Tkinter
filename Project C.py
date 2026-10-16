n=4

guess = input("Total points: 1 + 2 + 3 + 4")

input("Formula:one calculation. Press Enter to run ")
total = n * (n + 1) // 2
print("Total =", total, "steps = 1")

input("Loop: adds one student at a time.Press Enter to run")
total = 0
for student in range(1, n + 1):
    total += student
print("Total =", total, "steps =", n)

input("Double loop:"counts every single point. Press Enter to run")
total = 0
steps = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        total += 1
        steps += 1
print("Total =", total, "steps =", steps,"your guess was:", guess)

input("Double loop at n = 4 took 10 steps. Watch it grow. Press Enter")
for n in [10,100,1000]:
input("n = " + str(n) + ". Press Enter to run")
print ("steps = ", n * (n + 1) // 2)