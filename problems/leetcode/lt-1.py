# 1. Two Sum

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Input: [2, 7, 11, 15], target = 9
Output: [0, 1]
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkDict = {}
        for i in range(len(nums)):
            if nums[i] in checkDict:
                return [i, checkDict[nums[i]]]
            else:
                checkDict[target - nums[i]] = i