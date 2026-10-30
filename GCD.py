numberLargest = int(input("Enter Largest Number"))
numberSmallest = int(input("Enter smallest number"))

while(numberSmallest):
    numberStore = numberSmallest
    numberSmallest = numberLargest % numberSmallest
    numberLargest = numberStore
print("HCF is:", number largest)    