# 1640. Check Array Formation Through Concatenation
"""
    You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. 
    Your goal is to form arr by concatenating the arrays in pieces in any order. 
    However, you are not allowed to reorder the integers in each array pieces[i].
    Return true if it is possible to form the array arr from pieces. Otherwise, return false.

    Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
    Output: true
    Explanation: Concatenate [91] then [4,64] then [78]
"""
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        check_dict = dict()
        final_list = list()
        
        # Create the cache dictionary
        for piece in pieces:
            check_dict[piece[0]] = piece
            
        # Loop over and check for the presence of values
        for val in arr:
            if val in check_dict:
                final_list += check_dict[val]
            else:
                pass
        
        return arr == final_list