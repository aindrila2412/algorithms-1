"""
Function that determines the index of the smallest element of the cyclically shifted array.

Input:[4, 5, 6, 7, 9, 1, 3]
Output: 1
"""
def smallest_cyclic_array(arr):
	low = 0
	high = len(arr) - 1

	while low < high:
		mid = (low + high) // 2

		# If mid index value is greater than the high index value,
		# then the smallest value might be in the right side.
		if arr[mid] > arr[high]:
			low = mid + 1
		# If mid index value is smaller or equal to the high index value, 
		# then the smallest value might be in the left side
		elif arr[mid] <= arr[high]:
			high = mid

	return arr[low]

print(smallest_cyclic_array([4, 5, 6, 7, 9, 1, 3]))
