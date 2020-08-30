"""
Given an array of nn distinct integers sorted in ascending order, 
write a function that returns a fixed point in the array. 
If there is not a fixed point, return None.
"""
def fixed_point(arr):
	low = 0
	high = len(arr) - 1

	while low <= high:
		mid = (low + high) // 2

		if arr[mid] < mid:
			low = mid + 1

		elif arr[mid] > mid:
			high = mid - 1

		else:
			return arr[mid]

	return None

print(fixed_point([1, 2, 5, 8, 17]))
