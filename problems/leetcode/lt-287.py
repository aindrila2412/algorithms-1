# 287. Find the Duplicate Number
"""
    Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only constant extra space.

    Input: nums = [3,1,3,4,2]
    Output: 3
"""
# Time Complexity: O(n)
# Space Complexity = O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Using Floyd Cycle detection
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break 
            
        fast = nums[0]
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        print(slow, fast)
            
        return fast