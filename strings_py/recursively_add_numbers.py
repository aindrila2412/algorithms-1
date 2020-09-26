"""
Multiply two numbers recursively with minimum recursive calls.
"""
def recursive_multiply(x, y):
	# Inverting the varibales as (1000) 50 >> (50) 1000 reursive calls 
	if x < y:
		return recursive_multiply(y, x)

	if y == 0:
		return 0

	return x + recursive_multiply(x, y - 1)

print(recursive_multiply(1000, 50))