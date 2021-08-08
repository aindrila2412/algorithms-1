# 1464. Maximum Product of Two Elements in an Array
"""
    Given the array of integers nums, you will choose two different indices i and j of that array.
    Return the maximum value of (nums[i]-1)*(nums[j]-1).
"""
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Two ways: sort or min heap 

        # METHOD 1
        hashMap = dict()
        status = list()
        # Construction of a hashmap 
        for index, val in enumerate(mat):
            if val.count(1) not in hashMap.keys():
                hashMap[val.count(1)] = [index] 
            else:
                hashMap[val.count(1)].append(index)
        values = sorted(hashMap.keys())
        print(hashMap)
        for i in values:
            status += hashMap[i]
        return status[:k]
        
        # METHOD 2
        # Construction of a hashMap 
        hashMap = dict()
        status = list()
        values = list()
        for index, val in enumerate(mat):
            values.append(val.count(1))
            if val.count(1) not in hashMap.keys():
                hashMap[val.count(1)] = [index]
            else:
                hashMap[val.count(1)].append(index)
        heapq._heapify_max(values) 
        top3 = heapq.nsmallest(k, values)
        for i in set(top3):
            status += hashMap[i]
        return status[:k]
        