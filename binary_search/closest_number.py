"""
Given an array sorted in ascending order. Task is to find a number in the array that is closest 
to the target number using binary search.
"""
def closest_number(arr, target):
	minimum_difference = float('inf')
	low = 0
	high = len(arr) - 1
	final_value = None 

	# Handling edge cases 
	if len(arr) == 0:
		return None

	if len(arr) == 1:
		return arr[0]

	while low <= high:
		# Temporary left and right values to the mid values 
		mid = (low + high) // 2

		"""
		To ensure we don’t go out of bounds of the list, we check if mid+1 is less than the length of arr, 
		only then we access the element on the position mid+1. We take the absolute of the difference as we want
		the minimum difference with the closest number. 
		"""
		if mid + 1 < len(arr):
			main_difference_right = abs(arr[mid + 1] - target)

		"""
		To ensure we don’t go out of bounds of the list, we check if mid-1 is less than the length of arr, 
		only then we access the element on the position mid-1. We take the absolute of the difference as we want
		the minimum difference with the closest number. 
		"""
		if mid > 0:
			main_difference_left = abs(arr[mid -1 ] - target)

		"""
		The smaller among the left and right would be considered as the minimum difference and 
		final value would be updated accordingly as arr[mid+1] or arr[mid-1]
		"""
		if main_difference_left < minimum_difference:
			minimum_difference = main_difference_left
			final_value = arr[mid - 1]

		if main_difference_right < minimum_difference:
			minimum_difference = main_difference_right
			final_value = arr[mid + 1]

		"""
		Move the mid-point appropriately as is done
        via binary search.
  		"""
		if arr[mid] < target:
			low = mid + 1

		elif arr[mid] > target:
			high = mid - 1

		# If the element itself is the target, the closest
        # number to it is itself. Return the number.
		else:
			return arr[mid]

	return final_value

input_array = [1, 2, 4, 5, 6, 6, 8, 9]
print(closest_number(input_array, 11))