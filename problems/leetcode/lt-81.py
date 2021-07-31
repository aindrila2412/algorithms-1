# 81. Search in Rotated Sorted Array II
"""
    There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

    Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

    Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

    You must decrease the overall operation steps as much as possible.

    Input: nums = [2,5,6,0,0,1,2], target = 0
    Output: true
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        last = len(nums) - 1
        
        # Handle edge case 
        if len(nums) == 1:
            if nums[start] == target:
                return 1
            else:
                return 0
        
        # Binary search on the array, no need to find for minimum element index as there are duplicates
        while start < last:
            mid = (start + last) // 2
            
            # Retrun true if target is found
            if nums[mid] == target or nums[start] == target or nums[last] == target:
                return True 
            
            # Case when the target could be on the right side of the array
            if nums[mid] < nums[last]:
                if nums[mid] < target <= nums[last]:
                    start = mid + 1 
                else:
                    last = mid - 1
            
            # Case when the target could be on the left side 
            elif nums[mid] > nums[last]:
                if nums[mid] > target >= nums[start]:
                    last = mid - 1
                else:
                    start = mid + 1

            # Case when there are duplicates on both sides        
            else:
                last -= 1
            
            # Check if the low element has the target
            if nums[start] == target:
                return True
            
        return False
