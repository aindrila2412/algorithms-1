# 168. Excel Sheet Column Title
"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.
"""
class Solution:
    def convertToTitle(self, n: int) -> str:
        letters = string.ascii_uppercase 
        final = ""

        while n:
            remainder = n % 26 
            final = letters[remainder - 1] + final 
            
            if not remainder:
                n = n - 1
            n //= 26
            
        return final