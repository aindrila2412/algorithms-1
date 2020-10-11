"""
Determine if a string is a palindrome permutation.

Input: "picaoacip"
Output: True
"""
def palindrome_permutation(input):
	input = input.replace(" ", "").lower()
	check_dict = dict()

	# Create the dictionary for the characters of the input string 
	for i in input:
		if i not in check_dict:
			check_dict[i] = 1
		else:
			check_dict[i] += 1

	# A string that has an even length must have all even counts of characters, 
	# while strings that have an odd length must have exactly one character with an odd count. 
	# An even-length-ed string can’t have an odd number of exactly one character; otherwise, it wouldn’t
	# be even. This is true since an odd number plus any set of even numbers will yield an odd number.
	odd_count = 0
	for key, value in check_dict.items():
		if value % 2 != 0 and odd_count == 0:
			odd_count = 1
		elif value % 2 != 0 and odd_count != 0:
			return False 
	return True


print(palindrome_permutation('This is lame string'))
