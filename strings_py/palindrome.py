"""
Check if the string is a palindrome or not
"""
def palindrome(s):
	i = 0 
	j = len(s) - 1
	while i < j:
		if s[i].lower() != s[j].lower():
			return False 
		i += 1
		j -= 1
	return True 
print(palindrome('$haah$'))