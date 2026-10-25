scores = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

input("List: "+str(scores) + " n= 9 Press Enter to continue...")
guess = input("Max checks to find any number in the list: ")
target = int(input("Pick a number from the list: "))

input("Binary Search - Checks the middle, drops half each round. Press Enter")
low, high = 0, len(scores) - 1
steps = 0
while low <= high:
    mid = (low + high) // 2
    steps += 1
    print("round", steps, "-> checked" , scores[mid])
    if scores[mid] == target:
        print("Found", target, "in", steps, "steps")
        break
    elif scores[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
print(" found ", target, "at position", mid + 1, "in", steps, "steps your guess:", guess, "  -> O( log n)")   

input("Steps grow slowly with n. Press Enter to continue...")
for n,s in[0,4], [1,4], [2,4], [3,4], [4,4], [5,4], [6,4], [7,4], [8,4], [9,4]:
    print("n=", n, "steps=", s)     