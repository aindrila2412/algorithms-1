# 342. Power of Four
"""
    Given an integer n, return true if it is a power of four. Otherwise, return false.
    An integer n is a power of four, if there exists an integer x such that n == 4x.
"""
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        count = 0
        n = num
        if num < 1:
            return False 
        while (num > 1):
            num = num >> 2
            count += 2
        return (num << count) == n
        