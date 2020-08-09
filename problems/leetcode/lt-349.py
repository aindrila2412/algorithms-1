# 349. Intersection of Two Arrays

"""
Given two arrays, write a function to compute their intersection.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Faster 
        return set(nums1).intersection(set(nums2))
        
        # A little slow
        def get_intersections(setA, setB):
            return [x for x in setA if x in setB]
        
        setA = set(nums1)
        setB = set(nums2)
        
        if len(setA) < len(setB):
            return get_intersections(setA, setB)
        else:
            return get_intersections(setB, setA)