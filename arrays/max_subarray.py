"""
	
"""
# Method 1
# Kadane Algorithm (DP)
# Time complexity: O(n)
# Space complexity: O(1)
def maximum_subarray(nums):
	# Initialise the max value at the current position as the first element
	max_end = nums[0]
	# Initialise the max value in the entire sub array as the first element
	max_value = nums[0]

	# Loop from position to 1 to the length of the nums array
	for i in range(1, len(nums)):
		"""
		max_end takes the maximum value among the max_end + nums[i] (extend the previous subarray best whatever it was)
		max_value takes the max value among max_end and max_value and gives the final maximum subarray sum
		"""
		max_end = max(max_end + nums[i], nums[i])
		max_value = max(max_end, max_value)
	return max_value


# Method 3 (Naive)
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


# # Method 3
# # Time complexity: O(n^2)
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
