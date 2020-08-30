"""
Given an array that is bitonically sorted, an array that starts off with increasing terms and 
then concludes with decreasing terms. In any such sequence, there is a “peak” element which is 
the largest element in the sequence. Write a method to find the peak element.
"""
def bitonic_peak(arr):
	low = 0
	high = len(arr) - 1

	while low <= high:
		mid = (low + high) // 2

		if arr[mid - 1] < arr[mid] and arr[mid] < arr[mid + 1]:
			low = mid + 1
		elif arr[mid - 1] > mid and arr[mid] > arr[mid + 1]:
			high = mid - 1
		else:
			return arr[mid]

	return None 
print(bitonic_peak([ 1, 6, 5, 4, 3, 2, 1]))