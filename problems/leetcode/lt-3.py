# 3. Longest Substring Without Repeating Characters
"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    # Solution 1 (Hashmap)
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialise empty hasmap
        check_dict = dict()
        # Initialise the temporary check and final variable
        max_value = 0
        max_check = -1
        
        # If there are just 1 charcter or an empty string, return the length of it 
        if len(s) < 2:
            return len(s)
        
        # Iterate over the range of the string length
        for i in range(len(s)):
            # If the character exists in the hashmap, update the value of the temporary check variale
            if s[i] in check_dict:
                max_check = max(max_check, check_dict[s[i]])
            # Else, append the character to the hashmap
            check_dict[s[i]] = i    
            # The final value would be the max of max_value and current location - location of the found character
            max_value = max(max_value, i - max_check)
        return max_value

    # Solution 2 (Strings)
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialise empty string 
        check_str = ""
        # Initialise the final value as 0 
        max_value = 0
        # Iterate through the string
        for i in s:
            # If the character is not the character string, add it to it 
            if i not in check_str:
                check_str += i 
            else:
                # Otherwise, the maximum length would be the max of max_value and the length of the string 
                max_value = max(max_value, len(check_str))
                # Update the string by removing the characters before the found character inclusive of it from
                # the character and append the character after 
                check_str = check_str[check_str.index(i) + 1: ] + i
            
        return max(max_value, len(check_str))
                
    
        