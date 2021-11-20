# 416. Partition Equal Subset Sum
"""
    Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets 
    such that the sum of elements in both subsets is equal.

    Input: nums = [1,5,11,5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].
"""
# Approach 1, using DP top down
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Approach #1, DP
        # Time: O(n^2)
        # Space: O(n)

        nums_sum = sum(nums)
        # Handle edge case
        if nums_sum % 2 != 0:
            return False
        
        # Initialize dp array
        length = len(nums)
        max_sum = nums_sum // 2
        dp = [[-1 for i in range(max_sum + 1)] for j in range(length + 1)]

        # Initialise dp array with True and False  
        for i in range(length + 1):
            for j in range(max_sum + 1):
                if i == 0:
                    dp[i][j] = False
                if j == 0:
                    dp[i][j] = True
        
        # Check if sum of elements in subset is equal to max_sum
        for i in range(1, length + 1):
            for j in range(1, max_sum + 1):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
                if nums[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]

        # Return True if dp[length][max_sum] is True, coz the next set will equal to max_sum anyways
        return dp[length][max_sum]

# Approach 2, using Memoization 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def recursive_helper(nums, max_sum, length):
            if max_sum < 0:
                return False 
            if max_sum == 0:
                return True
            if length == 0:
                return False
            
            if dp[length][max_sum] != -1:
                return dp[length][max_sum]

            if nums[-1] <= max_sum:
                dp[length][max_sum] = recursive_helper(nums[:-1], max_sum - nums[-1], length - 1) or recursive_helper(nums[:-1], max_sum, length - 1)
                return dp[length][max_sum]

            if nums[-1] > max_sum:
                dp[length][max_sum] = recursive_helper(nums[:-1], max_sum, length - 1)
                return dp[length][max_sum]
        
        total_sum = sum(nums)
        if total_sum % 2 != 0: 
            return False
        
        max_sum = total_sum // 2
        dp = [[-1 for i in range(max_sum + 1)] for j in range(len(nums) + 1)]
        return recursive_helper(nums, max_sum, len(nums))


# Approach 3, using dfs 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def recursive_helper_dfs(numss, max_sum, values, length):
            if max_sum < 0:
                return False 
            if max_sum == 0:
                return True
            if length == 0:
                return False
            if max_sum in values:
                return False
            values.add(max_sum)

            for i in range(len(numss)):
                if recursive_helper_dfs(numss[i+1:], max_sum - numss[i], values, length - 1):
                    print(numss, '\n')
                    return True
            return False
            
        values = set()
        total_sum = sum(nums)
        max_sum = total_sum // 2
        if total_sum % 2 != 0:
            return False
        return recursive_helper_dfs(nums, max_sum, values, len(nums))