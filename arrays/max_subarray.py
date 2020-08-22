"""
	
"""

# Method 1 (Naive)
# Time complexity: O(n^3)
def maximum_subarray(nums):
	# Arbitary maximum sum
	maximum_sum = -1000000

	for i in range(0, len(nums)):
		for j in range(i, len(nums)):
			temp_sum = 0

			for k in range(i, j + 1):
				temp_sum += nums[k]
			maximum_sum = max(maximum_sum, temp_sum)

	return maximum_sum


# Method 2
# Time complexity: O(n^2)
def maximum_subarray(nums):
	# Arbitary maximum sum 
	maximum_sum = -100000

	for i in range(0, len(nums)):
		temp_sum = 0
		for j in range(i, len(nums)):
			temp_sum += nums[j]
			maximum_sum = max(maximum_sum, temp_sum)
	return final



print(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]))
