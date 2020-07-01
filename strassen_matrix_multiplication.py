# Implementation of Strassen Subcubic Matrix Multiplication

"""
    Naive Approach

    ---------
    Parameters
    ---------
    N number of matrices

    ---------
    Returns
    ---------
    Multiplied matrix

    ---------
    Time Complexity
    ---------
    O(n^3)

    ---------
    Test Cases
    ---------
    [1, 20, 6, 4, 5]
    => ([1, 4, 5, 6, 20], 5)

"""
def naiveStrassen(a, b, n):
    c = [[0, 0], [0, 0]]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] += a[i][k] * b[k][j]
    return c

a = [[1, 2], [3, 4]]
b = [[5, 6], [0, 7]]
n = 2

print(naiveStrassen(a, b, n))

"""
    Divide and Conquer Approach

    ---------
    Parameters
    ---------
    N number of matrices

    ---------
    Returns
    ---------
    Multiplied matrix

    ---------
    Time Complexity
    ---------
    O(n^3)

    ---------
    Test Cases
    ---------
    [1, 20, 6, 4, 5]
    => ([1, 4, 5, 6, 20], 5)

"""
