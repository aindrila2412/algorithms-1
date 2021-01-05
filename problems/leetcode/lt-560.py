# 560. Subarray Sum Equals K
"""
    Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
    Input: nums = [1,2,3], k = 3
    Output: 2   
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = 0
        check_dict = {0: 1}
        prefix_sum = 0
        # Loop over the length of the nums array
        for i in range(len(nums)):
            # Increment the prefix sum in each iteration
            prefix_sum += nums[i]
            
            # If prefix sum - k is already present in the cache dictionary, 
            # append the counter value equal to the number of times sum - k has occured.
            if prefix_sum - k in check_dict:
                counter += check_dict[prefix_sum - k]
            # Increment the cache dictionary counters
            if prefix_sum in check_dict:
                check_dict[prefix_sum] += 1
            else:
                check_dict[prefix_sum] = 1
                
        return counter 
            
            
        
        