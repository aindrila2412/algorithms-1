# 16. 3Sum Closest
"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        final_list = list()
        max_value = float('Inf')
        # Sort the nums array 
        nums.sort()
        for i in range(len(nums)):
            left = i + 1 
            right = len(nums) - 1 
            
            # Loop over until left index values is smaller than the right index value
            while left < right:
                # Check the difference of the sum of the three index values and target value
                difference = nums[i] + nums[left] + nums[right] - target
                # If the absolute value is less than the maximum value,
                # update the final array and maximum value 
                if abs(difference) < max_value:
                    max_value = min(abs(difference), max_value)
                    final_list = [nums[i], nums[left], nums[right]]
                # If the difference is 0, return the sum of the final array
                if difference == 0:
                    return sum(final_list)
                # If the difference is less than 0, increment the left index
                elif difference < 0:
                    left += 1 
                # If the difference is greater than 0, decrement the right index
                elif difference > 0:
                    right -= 1
                
        return sum(final_list)
        