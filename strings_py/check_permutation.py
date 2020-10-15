"""
Given two strings, return if one is the permutation of the other.

Input: str1 = "ooggle", str2 = "google"
Output: True
"""

# Time Complexity: O(n log n)
# Space Complexity: O(1)
def check_permutation_string_sorting(str1, str2):
	if len(str1) != len(str2):
		return False 

	str1 = "".join(sorted(str1)).lower()
	str2 = "".join(sorted(str2)).lower()

	if str1 == str2:
		return True 
	return False 
print(check_permutation_string_sorting('gooogle', 'ooggle'))


# Using a dictionary (Hash Table) 
# Time Complexity: O(n)
# Space Complexity: O(n)
def check_permutation_string_hash(str1, str2):
	if len(str1) != len(str2):
		return False 

	checkDict = dict() 

	# Convert into lowercase 
	str1 = str1.lower()
	str2 = str2.lower()

	for i in str1:
		if i not in checkDict:
			checkDict[i] = 1
		else:
			checkDict[i] += 1

	for i in str2:
		if i in checkDict:
			checkDict[i] -= 1
		else:
			checkDict[i] = 1

	return all(value == 0 for value in checkDict.values())

print(check_permutation_string_hash('google', 'ooggle'))



