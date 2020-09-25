"""
Given a string, calculate its length
"""

# Iterative approach 
def iterative_length(string):
	length = 0
	for i in string:
		length += 1

	return length 

print(iterative_length('hello worLd'))

# Recursive approach 
def recursive_length(string):
	if string == "":
		return 0 
	return 1 + recursive_length(string[1:])

print(recursive_length('hello Worlds'))
