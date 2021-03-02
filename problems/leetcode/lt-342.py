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

        # O(1) solution
        # Make sure only 1 set bit is there and %3 always give 1
        return (num > 0) and ((num & (num - 1)) == 0) and (num % 3 == 1)

        # Another O(1) solution as 10101010 (set bits are on odd places only in power of 2)
        # Make sure only 1 bit is set and that bit is on the odd place
        return (num > 0) and ((num & (num - 1)) == 0) and (num & 0xaaaaaaaa  == 0)
        