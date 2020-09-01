"""
A fuunction that takes an array of sorted integers and a key and 
returns the index of the first occurrence of that key from the array.

Input: [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 18
Output: 3
"""
def first_entry(arr, target):
	low = 0
	high = len(arr) - 1

	while low <= high:
		mid = (low + high) // 2

		if target < arr[mid]:
			high = mid - 1
		elif target > arr[mid]:
			low = mid + 1
		else:
			if mid - 1 < 0:
				return mid 
			if arr[mid - 1] != target:
				return mid
			high = mid - 1
	return None

print(first_entry([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 108))