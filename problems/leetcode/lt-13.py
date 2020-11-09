# 13. Roman to Integer 
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

For example, 2 is written as II in Roman numeral, just two one's added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, 
which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, 
the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

"""
class Solution:
    def romanToInt(self, s: str) -> int:
        # Dictionary with all the mappings 
        checkDict = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
        
        # Initial output as the value equivalent to the last character of the string
        output = checkDict[s[-1]]
        
        # Loop over from the end to the start of the string
        for i in range(len(s) - 2, -1, -1):
            # If the value equivalent to the current character is smaller than the next,
            # then, dubtract the values 
            if checkDict[s[i + 1]] > checkDict[s[i]]:
                output -= checkDict[s[i]]
            else:
                # Else, add the values to the output list
                output += checkDict[s[i]]
                
        return output
            
        