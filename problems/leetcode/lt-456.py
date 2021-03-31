# 456. 132 Pattern
"""
    Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] 
    such that i < j < k and nums[i] < nums[k] < nums[j].

    Return true if there is a 132 pattern in nums, otherwise, return false.

    Follow up: The O(n^2) is trivial, could you come up with the O(n logn) or the O(n) solution?

    Input: nums = [3,1,4,2]
    Output: true
    Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
"""
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # Initialzed the stack
        stack = []

        # Handling the edge case, if there are less than 3 elements
        if len(set(nums)) < 3:
            return False
        # Precomputing the minimum value array with first index same as first index of nums array 
        # to get arr[i] in O(1)
        minVal = [nums[0]]
        for i in range(1, len(nums)):
            minVal.append(min(nums[i], minVal[-1]))
        
        # Loop over for "j" index from right to left as "i"th index is fixed and can be taken from minVal
        for i in range(len(nums) - 1, -1, -1):
            # If the ith element is greater than the minimim ith element then only move forward
            if nums[i] > minVal[i]:
                # Remove the value from the top of the stack if "arr[k]" is smaller than the minimum
                while stack and stack[-1] <= minVal[i]:
                    stack.pop()
                # If arr[i] < arr[k] < arr[j], return True
                if stack and minVal[i] < stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False
