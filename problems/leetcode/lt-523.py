# 523. Continuous Subarray Sum
"""
    Given a list of non-negative numbers and a target integer k, 
    write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, 
    that is, sums up to n*k where n is also an integer.
"""
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
            sum(ar[i:j]) = sum(ar[j]) - sum(ar[j])
            Also, as we need to find for the arr_sum % k holds true or not,
            We can save  as arr_sum % k, and sum(ar[j]) - sum(ar[i]), such that;
            sum(ar[j]) = x * k + c 
            sum(ar[i]) = y * k + d
            sum(ar[i:j)) =  (x-y) * k + (c-d)
            So, we want to check for c = d 
        """
        # Initialise cache dictionary with key as sum 0 and value as index -1 
        checkDict = {0: -1}
        # Initialise the prefix sum as 0 
        prefix_sum = 0
        # Loop over the nums array 
        for i in range(0, len(nums)):
            # Increment the sum from index 0 to i
            prefix_sum +=  nums[i]
            if k != 0:
                # Take only the remainder to store in cache
                prefix_sum = prefix_sum % k 
            # If the remainder is present as a key in the cache dictionary
            if prefix_sum in checkDict:
                # Check if the difference between both the indexes is more than 1, return True
                if i - checkDict[prefix_sum] >= 2:
                    return True 
            else:
                # Otherwise, create a key value pair in the cache 
                checkDict[prefix_sum] = i
        return False 