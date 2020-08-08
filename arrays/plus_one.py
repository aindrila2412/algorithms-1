"""
Given an array of non-negative digits that represent a decimal integer.

Add one to the integer. Assume the solution still works even if 
implemented in a language with finite-precision arithmetic.

Input: [1, 4, 9]
Output: [1, 5, 0]
"""
def add_one(num_arr):
	carry = 1
	for i in range(len(num_arr) - 1, -1, -1):
		element = num_arr[i] + carry
		if element > 9:
			num_arr[i] = element % 10
			carry = 1
		else:
			num_arr[i] = element 
			carry = 0
	if carry == 1:
		num_arr = [1] + num_arr
	return num_arr 

print(add_one([9, 9, 9]))

# Method 2
def add_one(num_arr):
    num_arr[-1] += 1
    for i in reversed(range(1, len(num_arr))):
        if num_arr[i] != 10:
            break
        num_arr[i] = 0
        num_arr[i-1] += 1
    if num_arr[0] == 10:
        num_arr[0] = 1
        num_arr.append(0)
    return num_arr

print(add_one([9, 9, 9]))

# Method 3, inbuilt 
A = [1, 4, 9]
s = ''.join(map(str, A))
 print(int(s) + 1)