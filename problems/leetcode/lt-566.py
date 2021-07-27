# 566. Reshape the Matrix
"""
    In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

    You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

    The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

    If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.
"""
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat) * len(mat[0]) != r * c:
            return mat
        
        single_matrix = [None] * (len(mat) * len(mat[0]))
        new = []
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                n = len(mat[i])
                single_matrix[n*i+j] = mat[i][j]
                
        # Convert into the respective format 
        k = 0
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(single_matrix[k])
                k += 1
            new.append(temp)

        return new
        