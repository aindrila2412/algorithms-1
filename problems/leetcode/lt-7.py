# 7. Reverse Integer
"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 
32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
"""
class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False 
        value = 0
        
        # Check if the value is negative 
        if x < 0: 
            isNegative = True 
            x = -1 * x
            
        # Loop over and reverse the integer 
        while x > 0:
            remainder = x % 10 
            value = (value * 10) + remainder 
            x = x // 10
        
         # value should be in between 2^31 and -2^31, else return 0
        if value >= 2 ** 31 - 1 or value <= -2 ** 31:
            return 0
        
        if isNegative:
            return -1 * value 
        
        return value 
            
            
        
        
        