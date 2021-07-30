# 33. Search in Rotated Sorted Array
"""
    There is an integer array nums sorted in ascending order (with distinct values).

    Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.

    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(start, last):
            while start <= last:
                mid = (start + last) // 2
                if target == nums[mid]:
                    return mid 
                elif target < nums[mid]:
                    last = mid - 1
                else:
                    start = mid + 1
            return -1
        
        def get_minimum(start, last, n):
    # Calculate the minimum element index in the array O(log n)
            while start <= last:
                mid = (start + last) // 2
                prev = (mid + n - 1) % n 
                nextt = (mid + 1) % n

                if nums[mid] <= nums[prev] and nums[mid] <= nums[nextt]:
                    return mid 
                elif nums[mid] <= nums[last]:
                    last = mid - 1 
                elif nums[mid] >= nums[start]:
                    start = mid + 1

        last = len(nums) - 1
        start = 0
        found = -1 
        # Handling edge case 
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1 
            
        minimum = get_minimum(start, last, len(nums))
        # Finding the target in the first and second array pivot at the minimum element index O(log n)
        l1 = binary_search(0, minimum - 1)
        l2 = binary_search(minimum, last)
        if l1 != found:
            return l1
        if l2 != found:
            return l2
        else:
            return found