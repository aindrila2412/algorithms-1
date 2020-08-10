# Using hash table 
# Time Complexity: O(n)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        checkDict =dict()
        final = list()
        for i in nums1:
            if i not in checkDict:
                checkDict[i] = 1
            else: 
                checkDict[i] += 1
        for i in nums2:
            if i in checkDict:
                if checkDict[i] > 0:
                    final.append(i)
                    checkDict[i] -= 1
        return final

    # Time Complexity: O(m + n)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final = list()
        if len(nums1) < len(nums2):
            sl = nums1
            ll = nums2
        else:
            sl = nums2
            ll = nums1

        for i in range(len(sl)):
          new = sl[i]
          if new in ll:
              ll.remove(new)
              final.append(new)
        return final
        

    # Using sorted list
    # Time Complexity: O(n*logn)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i, j = 0, 0
        intersection = list()
        nums1.sort()
        nums2.sort()

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


        
            
        