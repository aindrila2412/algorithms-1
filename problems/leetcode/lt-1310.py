# 1310. XOR Queries of a Subarray
"""
    Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri], 
    for each query i compute the XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ). 
    Return an array containing the result for the given queries.

    Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
    Output: [2,7,14,8] 
    Explanation: 
    The binary representation of the elements in the array are:
    1 = 0001 
    3 = 0011 
    4 = 0100 
    8 = 1000 
    The XOR values for queries are:
    [0,1] = 1 xor 3 = 2 
    [1,2] = 3 xor 4 = 7 
    [0,3] = 1 xor 3 xor 4 xor 8 = 14 
    [3,3] = 8
"""
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        final = list()
        prefix_array = []
        prefix_array.append(arr[0])
        # Generate prefix array values 
        for val in range(1, len(arr), 1):
            temp_val = arr[val] ^ prefix_array[val-1]
            prefix_array.append(temp_val)
            
        # Generate the program to make xor for the specific query
        for index in range(0, len(queries), 1):
            left = queries[index][0]
            right = queries[index][1]
            if left == 0:
                final.append(prefix_array[right])
            else:
                xor_value = prefix_array[left - 1] ^ prefix_array[right]
                final.append(xor_value)
            
        return final
            
        