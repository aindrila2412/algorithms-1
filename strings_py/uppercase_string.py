"""
Develop an algorithm to return the first occurring uppercase letter. 
Use both iterative and recursive approach for the solution.
"""

# Iterative Approach 
def iterative_uppercase(string):
	for i in string:
		if i.isupper():
			return i 
	return "No Uppercase letter found!"


print(iterative_uppercase("hello World"))


# Recursive approach 
def recursive_uppercase(string, index = 0):
	if string[index].isupper():
		return string[index]
	if index == len(string) - 1:
		return "No uppercase letter found"

	return recursive_uppercase(string, index+1)

print(recursive_uppercase('hello worLd'))




