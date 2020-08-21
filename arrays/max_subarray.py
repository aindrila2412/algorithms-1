"""
Finding the maximum sub arrays inside a list
"""

def maximum_subarray(nums):
	# Arbitary maximum sum
	maximum_sum = -1000000
	final = []

	for i in range(0, len(nums)):
		for j in range(i, len(nums)):
			temp_sum = 0
			temp_arr = []

			for k in range(i, j + 1):
				temp_sum += nums[k]
				maximum_sum = max(maximum_sum, temp_sum)
				temp_arr.append(k)
			final.append(temp_arr)
	return final

print(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]))
