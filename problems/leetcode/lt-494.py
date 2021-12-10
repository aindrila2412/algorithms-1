# 494. Target Sum
"""
    You are given an integer array nums and an integer target.

    You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
    Return the number of different expressions that you can build, which evaluates to target.

    Input: nums = [1,1,1,1,1], target = 3
    Output: 5
    Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
    -1 + 1 + 1 + 1 + 1 = 3
    +1 - 1 + 1 + 1 + 1 = 3
    +1 + 1 - 1 + 1 + 1 = 3
    +1 + 1 + 1 - 1 + 1 = 3
    +1 + 1 + 1 + 1 - 1 = 3
"""
from collections import Counter
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def findTargetSum_helper(nums, max_sum, length):
            item_count = Counter(nums)
            zero_count = item_count[0]
            table = [[0 for i in range(max_sum + 1 )] for j in range(length + 1)]
            for i in range(length + 1):
                for j in range(max_sum + 1):
                    if i == 0:
                        table[i][j] = 0
                    if j == 0:
                        table[i][j] = 1

            for i in range(1, length + 1):
                for j in range(1, max_sum + 1):
                    if nums[i - 1] > j or nums[i - 1] == 0:
                        table[i][j] = table[i - 1][j]
                    else:
                        table[i][j] = table[i - 1][j] + table[i - 1][j - nums[i - 1]]
            # Multiplying the value by the 2 ** number of zeros
            return pow(2, zero_count) * table[length][max_sum]
        # Return 0 if the target is greater than the sum or the (target + sum) is odd
        if target > sum(nums) or (target + sum(nums)) % 2 != 0:
            return 0
        else:
            if len(nums) == 1 and nums[0] != abs(target):
                return 0
            max_sum = ((target + sum(nums)) // 2)
            count = findTargetSum_helper(nums, max_sum, length=len(nums))
            return count
