# Binary Search 

"""
Assumes array as sorted in ascending order. 

	- Iterative approach
	- Recursive approach
"""

# Iterative appraoch
def iterative_binary_search(arr, target):
	low = 0
	high = len(arr) - 1

	while low <= high:
		mid = (low + high) // 2
		if target == arr[mid]:
			return True
		elif target < mid:
			high = mid - 1
		else:
			low = mid + 1
	return False

print(iterative_binary_search([-1,2,3,4,5,6,7,9], -1))


