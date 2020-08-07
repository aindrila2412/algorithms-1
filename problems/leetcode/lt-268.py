# 268. Missing Number
"""
Given an array containing n distinct numbers taken from `0, 1, 2, ..., n`, 
find the one that is missing from the array.

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Taking sum using the Gauss formula of n(n+1)/2 for N natural numbers 
        sums = ((len(nums))*(len(nums) + 1))//2
        return sums - sum(nums)
        
        
        # Naive approach with time complexity in O(n)
        for i in range(0, len(nums) + 1):
            if i not in nums:
                return i
        