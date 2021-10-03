# 78. Subsets
"""
    Given an integer array nums of unique elements, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.  

    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def subset_helper(numbers):
            if len(numbers) == 0:
                return [[]]
            value = subset_helper(numbers[1:])
            return value + [[numbers[0]] + val for val in value]

        final = subset_helper(nums)
        return final 
