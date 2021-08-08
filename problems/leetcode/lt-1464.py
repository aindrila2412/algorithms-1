# 1464. Maximum Product of Two Elements in an Array
"""
    Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # nums = sorted(nums)
        # return ((nums[-1] - 1) * (nums[-2] - 1))
        heapq.heapify(nums)
        values = heapq.nlargest(2,nums)
        return ((values[0] - 1) * (values[1] - 1))

        