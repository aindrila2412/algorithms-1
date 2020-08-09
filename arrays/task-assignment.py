"""
Task is to assign tasks [array] to workers [subarrays, pairs (a, b)] so that the time it takes to complete all the tasks 
is minimized given a count of workers and an array where each element indicates the duration of a task.
"""

# Method 1, pairing shortest task with the longest task 
# Using a sorted array
# Time Complexity: O(n*logn)
def task_assignment(nums):
	nums = sorted(nums)
	for i in range(len(nums) // 2):
		print(nums[i], nums[~i])

task_assignment([6, 3, 2, 7, 5, 5])

# Method 2 (3 pointers, provide us with just 1 set of pairs)
# This is valid if the string is sorted 
def task_assignment(nums):
	i, j, k = 0, 1, 0
	while k < len(nums) // 2:
		print(nums[i], nums[j])
		i += 2
		j += 2
		k += 1

task_assignment([6, 3, 2, 7, 5, 5])

# Method 3
# Generate all possible pairs, inefficient as enumerating every possible pair would require 
# n(n-1)/2 pairs where n is the number of tasks in the given array
​