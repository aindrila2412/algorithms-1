# 12. Integer to Roman
"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. 
Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        values = {
            1: 'I',
            10: 'X',
            100: 'C',
            1000: 'M'
        }
        start = 1 
        final = ""
        while num > 0:
            remainder = num % 10 
            num = int(num / 10)
            current_char = values[start]
            characters = current_char * remainder 
            final = characters + final 
            start = start * 10  
            
        # Replace the strings 
        final = final.replace("CCCCCCCCC","CM")
        final = final.replace("CCCCC", "D")
        final = final.replace("CCCC", "CD")
        final = final.replace("XXXXXXXXX", "XC")
        final = final.replace("XXXXX", "L")
        final = final.replace("XXXX", "XL")
        final = final.replace("IIIIIIIII", "IX")
        final = final.replace("IIIII", "V")
        final = final.replace("IIII", "IV")
        
        return final 
            
            
            
        