# 171. Excel Sheet Column Number
"""
Given a column title as appear in an Excel sheet, return its corresponding column number.
"""
class Solution:
    def titleToNumber(self, s: str) -> int:
        count = len(s) - 1
        final = 0
        for i in s:
            final += 26 ** count * (ord(i) - ord('A') + 1)
            count -= 1
        return final
            
        