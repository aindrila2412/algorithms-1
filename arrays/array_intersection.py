"""
Given two sorted arrays, A and B, determine their intersection. 
What elements are common to A and B?
Consider for both sorted and unsorted arrays
"""

# Method 1 (SORTED ARRAYS)
# Considering the arrays are sorted
# Time complexity: O(n)
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


# Method 2 (UNSORTED ARRAYS)
# Here arrays are not sorted, we will use two sets 
# Time complexity: O(m + n) where m and n are length of arrays 
def array_intersection(nums1, nums2):
	def get_intersecting_elements(setA, setB):
		return [x for x in setA if x in setB]

	setA = set(nums1)
	setB = set(nums2)

	if len(setA) < len(setB):
		return get_intersecting_elements(setA, setB)
	else:
		return get_intersecting_elements(setB, setA)



# Method 2 (Using in-built methods)
# def array_intersection(nums1, nums2):
# 	print(set(nums1).intersection(nums2))

array_intersection([3, 3, 7, 15, 31], [2, 3, 3, 5, 7, 11])