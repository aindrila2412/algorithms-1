"""
Is it possible to advance from the start of the array to the last element given that 
the maximum you can advance from a position is based on the value of the array at the index 
you are currently present on?

Input: [3,3,1,0,2,0,1]
Output: True
"""
def jump_into_array(nums):
	maximum_value = 0
	last_index = len(nums) - 1
	i = 0
	while i <= maximum_value and maximum_value < last_index:
		maximum_value = max(maximum_value, nums[i] + i)
		i += 1
	return maximum_value >= last_index


nums = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(nums))
# Output: False: Not possible to navigate to last index in nums array.
