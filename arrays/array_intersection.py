"""
Given two sorted arrays, A and B, determine their intersection. 
What elements are common to A and B?
"""

# Method 1
# Considering the arrays are sorted 
def array_intersection(nums1, nums2):
	i, j = 0, 0
	intersection = list()

	# Handle empty array
	if len(nums1) == 0:
		return intersection

	while i < len(nums1) and j < len(nums2):
		if nums1[i] == nums2[j]:
			# Check for unique elements 
			if nums1[i] != nums1[i-1] or i == 0:
				intersection.append(nums1[i])
			i += 1
			j += 1

		elif nums1[i] < nums2[j]:
			i += 1
		else:
			j += 1
	return intersection


# Method 2 (Using in-built methods)
# def array_intersection(nums1, nums2):
# 	print(set(nums1).intersection(nums2))

array_intersection([3, 3, 7, 15, 31], [2, 3, 3, 5, 7, 11])