# 697. Degree of an Array
"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the 
maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, 
that has the same degree as nums.

Input: nums = [1,2,2,3,1,4,2]
Output: 6
"""

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        check_dict = {}
        # Loop through the nums array and add the items with their positions to the hash table
        for i, num in enumerate(nums):
            if num not in check_dict:
                check_dict[num] = [i]
            else:
                check_dict[num].append(i)
        # Getting the key(s) with the maximum values 
        maximum_val = 0
        minimum_subarray_len = float('inf')
        final_arr = []
        for key, val in check_dict.items():
            if len(val) > maximum_val:
                maximum_val = len(val)
                final_arr = [key]
            elif maximum_val == len(val):
                final_arr.append(key)
                
        # Get the subarray length by findign the mimimum among last position - first position + 1
        # and the minimum subarray length (specially when 2 or more key has same max values)
        for i in final_arr:
            minimum_subarray_len = min((check_dict[i])[-1] - (check_dict[i])[0] + 1, minimum_subarray_len)
        
        return minimum_subarray_len
                