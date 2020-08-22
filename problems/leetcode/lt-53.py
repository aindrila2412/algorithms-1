# 53. Maximum Subarray
"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_end = nums[0]
        max_value = nums[0]
        
        for i in range(1, len(nums)):
            max_end = max(max_end + nums[i], nums[i])
            max_value = max(max_end, max_value)
        return max_value
            