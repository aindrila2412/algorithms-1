# 779. K-th Symbol in Grammar
"""
    We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, 
    we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

    For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
    Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.
    
    Input: n = 4, k = 6
    Output: 0
    Explanation:
    row 1: 0
    row 2: 01
    row 3: 0110
    row 4: 01101001
"""
import math
class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        # Base condition
        if N == 1:
            return 0 
        parent = self.kthGrammar(N - 1, math.ceil(K / 2))        
        isEven = K % 2 == 0
        if parent == 1:
            return 0 if isEven else 1
        else:
            return 1 if isEven else 0

# Tried creating all values, exceeds recursion branching

# def kthGrammar(n, k, values):
#     def insert_helper(values):
#         print(len(values))
#         if len(values) == 0:
#             return values 
#         temp = values[-1]
#         values.pop()
#         insert_helper(values)
#         if temp == 0:
#             values.append(0)
#             values.append(1)
#         else:
#             values.append(1)
#             values.append(0)

#     def helper(n, values):
#         if n == 1:
#             values.append(0)
#             return  values 
        
#         helper(n - 1, values)
#         insert_helper(values)
#     helper(n, values)
        

# values = []
# kthGrammar(12, 1, values)
# print(len(values))
