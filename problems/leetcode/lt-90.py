# 90. Subsets II
"""
    Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.

    Input: nums = [1,2,2]
    Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]    
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def subset_helper(numbers, f):
            if len(numbers) == 0:
                f.append([])
                return 
            subset_helper(numbers[1:], f)
            f += [sorted([numbers[0]] + val) for val in f if sorted([numbers[0]] + val) not in f]
            return
        
        f = []
        final = subset_helper(nums, f)
        return f