"""
Given a string, count the number of consonants using both iterative and recursive approach.
"""

# Iterative approach 
def iterative_consonants(string):
	vowels = 'aeiou'
	count = 0
	for i in string:
		if i.lower() not in vowels and i.isalpha():
			count += 1
	return count

print(iterative_consonants('Welcome to Strings!!!!'))


# Recursive apprach
def recursive_consonants(string):
	vowels = 'aeiou'
	if string == "":
		return 0

	if string[0].lower() not in vowels and string[0].isalpha():
		return 1 + recursive_consonants(string[1:])

	else:
		return recursive_consonants(string[1:])

print(recursive_consonants('Welcome to Strings!!!!'))


