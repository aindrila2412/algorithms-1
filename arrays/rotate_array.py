"""
Rotate an array with by `k` steps to the right.

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
"""

# Brute Force 
# Time complexity: O(n * k)
# Space complexity: O(1)
def brute_rotate_array(arr, k):
	k = k % len(arr)
	for i in range(k):
		previous = arr[-1]
		for j in range(len(arr)):
			temp = arr[j]
			arr[j] = previous 
			previous = temp
	return arr

print(brute_rotate_array([1, 2, 3, 4, 5, 6, 7], 2))

# Slicing with extra and no extra space
def slice_rotate_array(arr, k):
	k = k % len(arr)
	new_arr = []
	new_arr = arr[k:]+arr[:k]
	arr[:] = arr[-k:] + arr[:-k]
	return arr

print(slice_rotate_array([1, 2, 3, 4, 5, 6, 7], 2))

# Using Extra array 
# Time complexity: O(n)
# Space complexityL O(n)
def extra_rotate_array(arr, k):
	new_arr = [0] * len(arr)
	for i in range(len(arr)):
		new_arr[(i + k) % len(arr)] = arr[i]
	return new_arr

print(extra_rotate_array([1, 2, 3, 4, 5, 6, 7], 2))


# Using Reverse
# 1 -> Reverse the entire list
# 2 -> Reverse the first `k` elements 
# 3 -> Reverse the `n-k` elements
# Time complexity: O(n)
# Space complexity: O(n)
def reverse_rotate_array(arr, k):
	# Reverse an array 
	def reverse_helper(nums, start, end):
		while start < end:
			nums[start], nums[end] = nums[end], nums[start] 
			start += 1
			end -= 1
		return nums

	k = k % len(arr)
	arr = reverse_helper(arr, 0, len(arr) - 1)
	arr = reverse_helper(arr, 0, k - 1)
	arr = reverse_helper(arr, k, len(arr) - 1)

	return arr 

print(reverse_rotate_array([1, 2, 3, 4, 5, 6, 7], 2))

