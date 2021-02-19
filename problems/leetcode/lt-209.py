# 209. Minimum Size Subarray Sum
"""
Given an array of n positive integers and a positive integer s, 
find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
"""
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_length = float('inf')
        left = 0 
        temp_sum = 0
        
        # Loop over for sliding window 
        for i in range(len(nums)):
            temp_sum += nums[i]
            # Once the sum is greater than the given sum, start decrementing the value from the left 
            while temp_sum >= s:
                min_length = min(min_length, i + 1 - left)
                temp_sum -= nums[left]
                left += 1
        # return min_length if min_length < len(nums) + 1 else 0
        if min_length != float('inf'):
            return min_length
        else:
            return 0