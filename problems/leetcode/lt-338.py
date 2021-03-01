# 338. Counting Bits
"""
    Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's 
    in their binary representation and return them as an array.

    Input: 5
    Output: [0,1,1,2,1,2]
"""
class Solution:
    def check_count(self, value):
    #     count = 0 
    #     while value > 0: 
    #         if value & 1 > 0:
    #             count += 1 
    #         value = value >> 1
    #     return count 
        count = 0
        while value:
            count += 1
            value = value & (value - 1)
        return count
        
    def countBits(self, num: int) -> List[int]:
        output = list()
        for i in range(0, num + 1):
            value = self.check_count(i)
            output.append(value)
        return output