# 15. 3Sum
"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize an empty list for the final array 
        final_list = list() 
        # Sort the array 
        nums.sort()
        # Loop over the length of nums array 
        for i in range(len(nums)):
            # Initial sum such that inside the loop we find a 2sum which is equal to this and adding will give us a 0 value
            check_sum = -nums[i]
            left = i + 1 
            right = len(nums) - 1 
            
            # Edge case to skip if 2 consecutive same values are present 
            if i != 0 and nums[i] == nums[i-1]:
                continue 
            
            # Loop over until left index is smaller than the right index
            while left < right:
                if nums[left] + nums[right] == check_sum:
                    final_list.append([nums[i], nums[left], nums[right]])
                    
                    # Stop the loop from adding the duplicate values 
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1 
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    # Increment the pointers to move forward in the array
                    left += 1
                    right -= 1 
                
                elif nums[left] + nums[right] < check_sum:
                    left += 1 
                else:
                    right -= 1
        return final_list        
                
                
            
        