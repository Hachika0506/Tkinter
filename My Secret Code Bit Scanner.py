secret_code = 12
access_key = 4

def bits(number,width=4):
    return format(number & ((1<< width)-1), f'0{width}b')

print("====================")

#Part 1 - bits and Binary
print("Part 1 - bits and Binary")
print("Secret code Binary:", bits(secret_code))
print("Access key Binary:", bits(access_key))

#part 2 - AND and OR
and_result = secret_code & access_key
or_result = secret_code | access_key
print("====================")
print("Part 2 - AND and OR")
print("AND Result:", and_result,"Binary:", bits(and_result))
print("OR Result:", or_result,"Binary:", bits(or_result))

#Part 3 - NOT and XOR
not_result = ~secret_code & 0b1111  # Mask to keep only the last 4 bits
xor_result = secret_code ^ access_key

print("====================")
print("Part 3 - NOT and XOR")
print("NOT secret code within 4 bits:", not_result,"Binary:", bits(not_result))
print("XOR Result:", xor_result,"Binary:", bits(xor_result))
print("XOR gives 1 when the compared bits are different")

#Part 4 - LEFT SHIFT and RIGHT SHIFT
left_shift_result = secret_code << 1
right_shift_result = secret_code >> 1

print("====)===============")
print("Part 4 - LEFT SHIFT and RIGHT SHIFT")
print("Left Shift Result:", left_shift_result, "Binary:", bits(left_shift_result, width=5))
print("Left shift moves bits to the left, Right shift moves bits to the right")

#Part 5 - ODD or EVEN with XOR
xor_check = secret_code ^ 1

print("====================")
print("Part 5 - ODD or EVEN with XOR")
print("Secret code XOR 1:", xor_check)

if xor_check == secret_code - 1:
  print("Secret code is odd because XOR with 1 reduced it by 1")
else:
  print("Secret code is even because XOR with 1 increased it by 1")

#part 6 - Counting Bits
bit_count = secret_code.bit_count()
print("====================")
print("Part 6 - Counting Bits")
print("Number of 1 bits in secret code:", bit_count)
