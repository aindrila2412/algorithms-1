# 231. Power of Two
"""
    Given an integer n, return true if it is a power of two. Otherwise, return false.
    An integer n is a power of two, if there exists an integer x such that n == 2x.
""" 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False 
        count = 0
        while n:
            count += 1
            n = n & (n-1)
        if (count) == 1:
            return True 
        else:
            return False 
