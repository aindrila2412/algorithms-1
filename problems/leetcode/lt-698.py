# 698. Partition to K Equal Sum Subsets
"""
    Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets 
    whose sums are all equal.
"""
# Using backtracking and memoization 
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        visited = [False] * len(nums)
        def dfs(k, subset_sum, target, index):
            if k == 0:
                return True
            if subset_sum == target:
                print(visited)
                return dfs(k - 1, 0, target, 0)

            for i in range(index, len(nums)):
                if visited[i] or subset_sum + nums[i] > target:
                    continue 
                visited[i] = True
                if dfs(k, subset_sum + nums[i], target, i + 1):
                    return True
                visited[i] = False
            return False
        if sum(nums) % k != 0:
            return False
        else:
            return dfs(k, 0, sum(nums) // k, 0)