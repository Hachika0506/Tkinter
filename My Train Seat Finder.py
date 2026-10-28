seat_numbers = [10,15,20,25,30,35,40,45,50,55,60,65]
target_seat = 45

print("^^^^^^^^^^^^^^")
print("My Train Seat Finder")
print("^^^^^^^^^^^^^^")
print("Available seat numbers:")
print("Searching for seat number:", target_seat)

print("^^^^^^^^^^^^^^")
print("Part 1: Binary Search")
def binary_search(seat_numbers, target_seat):
    low = 0
    high = len(seat_numbers) - 1
    steps = 0
    while low <= high:
        steps = steps + 1
        mid = (low + high) // 2
        print("Checking middle seat number:", seat_numbers[mid])
        if seat_numbers[mid] == target_seat:
            print("Seat number found:", seat_numbers[mid])
            print("Total steps taken:", steps)
            return mid, steps
        elif target_seat < seat_numbers[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1, steps

index, steps = binary_search(seat_numbers, target_seat)

print("Binary Search Result:")
if index != -1:
    print("Seat number", target_seat, "found at index", index)
else:
    print("Seat number", target_seat, "seat not found.")

print("Steps Taken:", steps) 
print("Time Complexity: O(log n)")
print("Space Complexity: O(1)")      

print("^^^^^^^^^^^^^^")
print("Part 2: Recursive Binary Search")
def recursive_binary_search(seat_numbers, target_seat, low, high, steps=0):      
    if low > high:
        return -1

    mid = (low + high) // 2
    print("Recursively checking middle seat number:", seat_numbers[mid])

    if seat_numbers[mid] == target_seat:
        print("Seat number found:", seat_numbers[mid])
        print("Total steps taken:", steps + 1)
        return mid, steps + 1
    elif target_seat < seat_numbers[mid]:
        return recursive_binary_search(seat_numbers, target_seat, low, mid - 1)
    else:
        return recursive_binary_search(seat_numbers, target_seat, mid + 1, high)

recursive_index = recursive_binary_search(seat_numbers, target_seat, 0, len(seat_numbers) - 1)    
print("Recursive Binary Search Result:")
if recursive_index != -1:
    print("Seat number", target_seat, "found at index", recursive_index)
else:
    print("Seat number", target_seat, "seat not found.")

print("Recursive Time Complexity: O(log n)")
print("Recursive Space Complexity: O(log n) due to call stack")

print("^^^^^^^^^^^^^^")
print("Complexity Ladder:")
print("^^^^^^^^^^^^^^")
print("O(1): Directly checking one fixed seat ")
print("O(log n): Binary search by cuting the list in half ")
print("O(n): Checking every seat one by one ")
print("O(n^2): Comparing every seat with every other seat")
print("^^^^^^^^^^^^^^^^")