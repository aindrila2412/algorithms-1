# 41. First Missing Positive
"""
    Given an unsorted integer array nums, return the smallest missing positive integer.

    You must implement an algorithm that runs in O(n) time and uses constant extra space.

    Input: nums = [3,4,-1,1]
    Output: 2       

"""
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Converting all negatives to 0 
        for index, num in enumerate(nums):
            if num != abs(num):
                nums[index] = 0
        
        # Converting into negatives 
        for index, num in enumerate(nums):
            num = abs(num)
            if num <= len(nums) and num - 1 >= 0:
                num = abs(num)
                if nums[num - 1] == 0:
                    nums[num - 1] = -(abs(len(nums) + 1))
                else:
                    nums[num - 1] = -(abs(nums[num - 1]))
            
        # Checking for the missing positive value
        for i in range(len(nums)):
            if nums[i] == abs(nums[i]):
                print(i + 1)
                return i + 1
        
        return len(nums) + 1