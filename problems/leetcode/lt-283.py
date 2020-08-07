# 283. Move Zeroes

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, k = 0, 0
        while k < len(nums):
            if nums[i] == 0:
                # Pop the index value if it's equals to zero
                nums.pop(i)
                # Push a 0 value to the last index
                nums.append(0)
                k+= 1
            else:
                i += 1
                k += 1

        # Secondary solution is to sort the list 
        nums.sort(key = bool, reverse = 1)