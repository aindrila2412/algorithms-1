# 34. Find First and Last Position of Element in Sorted Array
"""
    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a 
    given target value.
    If target is not found in the array, return [-1, -1].
    You must write an algorithm with O(log n) runtime complexity.
    
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]
"""
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Edge cases when there the array is empty and has only single value
        if len(nums) == 0:
            return [-1, -1]
        if len(nums) == 1 and nums[0] == target:
            return [0, 0]

        # Doing a binary search to find the target value index  
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                break 
            if target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1 

        # Return [-1, -1] when target value isn't present
        if low > high:
            return [-1, -1]
        else:
            # Else, move to both sides of the array unless new value occurs
            l = mid 
            r = mid
            print(mid)
            while True:
                if l - 1 >= 0 and nums[l - 1] == nums[mid]:
                    l -= 1
                elif r + 1 <= len(nums) - 1 and nums[r + 1] == nums[mid]:
                    r += 1
                else:
                    break
            # Return the left and right index
            return [l, r]
        return [-1, -1]