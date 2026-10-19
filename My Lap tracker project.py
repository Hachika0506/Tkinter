n = 5
print("My running lap tracker")

# Solution Method 1: Formula Method
formula_total = n * (n + 1) // 2
print("Solution Method 1: Formula Method")
print("Total Running Points:", formula_total)
print("Time Complexity: O(1)")
print("Space Complexity: O(1)")
print()

# Solution Method 2: Loop Method
loop_total = 0
steps_loop = 0
for lap in range(1, n + 1):
    loop_total = loop_total + lap
    steps_loop = steps_loop + 1

print("Solution method 2: Loop Method")
print("Total Running Points:", loop_total)
print("steps Taken:", steps_loop)
print("Time Complexity: O(n)")
print("Space Complexity: O(1)")
print()

# Solution Method 3: Nested Loop Method
nested_total = 0
steps_nested = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        nested_total = nested_total + 1
        steps_nested = steps_nested + 1

print("Solution method 3: Nested Loop Method (Example Demonstration)")
print("Total Running Points (demonstration):", nested_total)
print("steps Taken:", steps_nested)
print("Time Complexity: O(n^2)")
print("Space Complexity: O(1)")
print()

print("*****************")
print("The Algorithm Efficiency Comparison")
print("*****************")
print("Formula Method: Fastest because it uses only 1 Calculation")
print("Loop Method: Slower because it repeats once for every lap")
print("Nested Loop Method: Slowest because it uses a loop inside another loop")
print()
print("Best Method: Formula Method")
print("Worst Method: Nested Loop Method")
print()