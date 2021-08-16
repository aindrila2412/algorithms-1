# 645. Set Mismatch
"""
    You have a set of integers s, which originally contains all the numbers from 1 to n. 
    Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, 
    which results in repetition of one number and loss of another number.

    You are given an integer array nums representing the data status of this set after the error.

    Find the number that occurs twice and the number that is missing and return them in the form of an array.

    Input: nums = [1,2,2,4]
    Output: [2,3]
"""
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Method 1: Using sorting 
        # Time complexity: O(n logn)
        # Space complexity: O(logn)
        nums.sort()
        duplicate = -1
        missing = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                duplicate = nums[i]
            elif nums[i] > nums[i - 1] + 1:
                missing = nums[i - 1] + 1
                
        if nums[len(nums) - 1] != len(nums):
            return [duplicate, len(nums)]
        else:
            return [duplicate, missing]

        # Method 2: Using hashmap 
        # Time complexity: O(n)
        # Space complexity: O(n)
        hashMap = dict()
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        duplicate = -1 
        missing = 1
        
        for i in range(1, len(nums) + 1):
            if i in hashMap:
                if hashMap[i] == 2:
                    duplicate = i 
            else:
                missing = i
        
        return [duplicate, missing ]

        # Method 3: Using negatives 
        # Time Complexity: O(n)
        # Space Complexity: 0(1)
        duplicate = -1
        missing = 1 
        for i, num in enumerate(nums):
            num = abs(num)
            if nums[num - 1] != abs(nums[num - 1]):
                duplicate = num
            nums[num - 1] = -(abs(nums[num - 1]))
            
        for i, num in enumerate(nums):
            if num == abs(num):
                missing = i + 1 
                
        return [duplicate, missing]