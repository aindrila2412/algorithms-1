# 1304. Find N Unique Integers Sum up to Zero
"""
    Given an integer n, return any array containing n unique integers such that they add up to 0.
"""
class Solution:
    def sumZero(self, n: int) -> List[int]:
        final = list()
        if n % 2 == 0:
            val = n // 2
            for i in range(-val, val + 1, 1):
                if i == 0:
                    pass
                else:
                    final.append(i)
        else:
            val = n // 2
            for i in range(-val, val + 1, 1):
                final.append(i)
        return final 