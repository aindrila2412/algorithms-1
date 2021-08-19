# 912. Sort an Array
"""
    Given an array of integers nums, sort the array in ascending order.
    Input: nums = [5,2,3,1]
    Output: [1,2,3,5]
"""
# Using Merge Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sorts(unsortedList):
            def merge_list(leftSideArray, rightSideArray):
                sorted_array = []
                while leftSideArray and rightSideArray:
                    sorted_array.append(
                        (leftSideArray if leftSideArray[0] <= rightSideArray[0] else rightSideArray).pop(0))
                return sorted_array + leftSideArray + rightSideArray
            if len(unsortedList) <= 1:
                return unsortedList
            midTerm = len(unsortedList) // 2
            return merge_list(merge_sorts(unsortedList[:midTerm]), merge_sorts(unsortedList[midTerm:]))

        return merge_sorts(nums)