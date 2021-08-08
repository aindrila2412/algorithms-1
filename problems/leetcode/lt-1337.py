# 1337. The K Weakest Rows in a Matrix
"""
    You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). 
    The soldiers are positioned in front of the civilians. 
    That is, all the 1's will appear to the left of all the 0's in each row.

    A row i is weaker than a row j if one of the following is true:

    The number of soldiers in row i is less than the number of soldiers in row j.
    Both rows have the same number of soldiers and i < j.
    Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.
"""
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # Two ways: sort or min heap 
        hashMap = dict()
        status = list()
        # Construction of a hashmap 
        for index, val in enumerate(mat):
            if val.count(1) not in hashMap.keys():
                hashMap[val.count(1)] = [index] 
            else:
                hashMap[val.count(1)].append(index)
        
        # Method 1
        values = sorted(hashMap.keys())
        print(hashMap)
        for i in values:
            status += hashMap[i]
        return status[:k]


        # Method 2
