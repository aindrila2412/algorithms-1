# 191. Number of 1 Bits
"""
    Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Approach 1 (right shift by 1 each time)
        count = 0
        while n > 0:
            if n & 1 > 0:
                count += 1
            n = n >> 1
        return count
    
        # Approach 2 (AND of val and val -1)
        count = 0
        while n:
            count += 1
            n = n & (n-1)
        return count 
            