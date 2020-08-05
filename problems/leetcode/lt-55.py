# 55. Jump Game

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Input: nums = [2,3,1,1,4]
Output: true
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maximum_jump = 0
        last_index = len(nums) - 1
        i = 0
        while i <= maximum_jump and maximum_jump < last_index:
            maximum_jump = max(maximum_jump, nums[i] + i)
            i += 1
        return maximum_jump >= last_index
    
            
        