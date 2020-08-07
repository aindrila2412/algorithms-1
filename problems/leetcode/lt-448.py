# 448. Find All Numbers Disappeared in an Array
"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), 
some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list 
does not count as extra space.

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Marking the index of the values as negative, and positive index is pushed to 
        # the new stack. Efficient in terms of memory
        final = list()
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            nums[temp] = abs(nums[temp]) * -1
            
        for i in range(len(nums)):
            if nums[i] > 0:
                final.append(i + 1)
        return final
        
        # Using Sets, efficint in terms of time complexity
        new_nums = set(nums)
        final = list()
        
        for i in range(1,len(nums) + 1):
            if i not in new_nums:
                final.append(i)
        return final
            
                
		# Using counter values (not efficinet, extra space)
        checkDict = {}
        finalList = list()
        for i in nums:
            if i not in checkDict:
                checkDict[i] = 1
            else:
                checkDict[i] += 1
        
        for i in range(1, len(nums) + 1):
            if i not in checkDict:
                finalList.append(i)
                
        return finalList
                
                
                
