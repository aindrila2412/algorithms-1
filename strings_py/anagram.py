"""
Check if two strings anagrams of each other 
"""
def anagram(str1, str2):
	checkDict = {}
	str1 = str1.replace(" ", "").lower()
	str2 = str2.replace(" ", "").lower()

	for i in str1:
		if i not in checkDict:
			checkDict[i] = 1
		else:
			checkDict[i] += 1

	for j in str2:
		if j in checkDict:
			checkDict[j] -= 1
		else:
			checkDict[j] = 1

	for k in checkDict:
		if checkDict[k] != 0:
			return False  
	return True 

s1 = "fairy tales"
s2 = "rail safety"
print(anagram(s1, s2))
