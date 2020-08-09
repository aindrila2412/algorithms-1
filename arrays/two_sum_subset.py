"""
Given an array of integers, return True or False if the array has two numbers that add up to a specific target.
You may assume that each input would have exactly one solution.

Input: [-2, 1, 2, 4, 7, 11], target=13
Output: True (2, 11)
"""

# Using two pointers (first and last index), assuming array is sorted
# Time complexity: O(n)
# Space complexity: O(1)
def two_sum_subset(nums, target):
	i, j = 0, len(nums) - 1
	while i < j:
		if nums[i] + nums[j] == target:
			print("Elements found: ", nums[i], nums[j])
			return True 
		elif nums[i] + nums[j] < target:
			i += 1
		else:
			j -= 1

two_sum_subset([-2, 1, 2, 4, 7, 11], 13)




# Nested loop (Not efficient)
# Time complexity: O(n^2)
# Space complexity: O(1)
def two_sum_subset(nums, target):
	for i in range(len(nums) - 1):
		for j in range(i + 1, len(nums)):
			if nums[i] + nums[j] == target:
				print("Elements: ", nums[i], nums[j])
				return True 
	return False

two_sum_subset([-2, 1, 2, 4, 7, 11], 13)


# Using Hash Table 
# Time Complexity: O(n)
# Space Complexity: O(n)
def two_sum_subset(nums, target):
	checkDict = dict()
	for i in range(len(nums)):
		if nums[i] in checkDict:
			print('Elements found: ', nums[i], checkDict[nums[i]])
			return True 
		else:
			checkDict[target - nums[i]] = nums[i]
	return False


two_sum_subset([-2, 1, 2, 4, 7, 11], 13)



