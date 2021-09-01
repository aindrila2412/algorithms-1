# 1636. Sort Array by Increasing Frequency
"""
    Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

    Return the sorted array.

    Input: nums = [1,1,2,2,2,3]
    Output: [3,1,1,2,2,2]
    Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.
"""
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        Solution 1: using sorting only 
        final = sorted(sorted(nums, reverse=True), key=nums.count)
        return final 
        
        # Solution 2: using hashmap and sorting 
        value_count = Counter(nums)
        value_common = value_count.most_common()
        value_common.sort(key=lambda x:x[0], reverse=True)
        value_common.sort(key=lambda x:x[1])
        final = list()
        for val in value_common:
            x, y = val
            final.extend([x] * y)
        return final
