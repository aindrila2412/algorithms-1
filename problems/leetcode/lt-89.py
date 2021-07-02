# 89. Gray Code
"""
    An n-bit gray code sequence is a sequence of 2n integers where:

        Every integer is in the inclusive range [0, 2n - 1],
        The first integer is 0,
        An integer appears no more than once in the sequence,
        The binary representation of every pair of adjacent integers differs by exactly one bit, and
        The binary representation of the first and last integers differs by exactly one bit.

    Given an integer n, return any valid n-bit gray code sequence.

    Input: n = 2
    Output: [0,1,3,2]
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        final = [0]
        check = set()
        check.add(0)
        
        if n == 0:
            return final
        
        for i in range(pow(2, n)):
            for j in range(n):
                if pow(2, j) ^ final[-1] not in check:
                    current = pow(2, j) ^ final[-1]
                    final.append(current)
                    check.add(current)
                    break 
        return final
        