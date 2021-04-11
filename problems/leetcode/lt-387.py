# 387. First Unique Character in a String
"""
    Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

    Input: s = "loveleetcode"
    Output: 2
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash_map = dict()
        
        # Add index as the value if it's unique, else -1
        for index, value in enumerate(s):
            if value not in hash_map:
                hash_map[value] = index 
            else:
                hash_map[value] = -1 
        
        # Iterate and check for the first non -1 value
        for val in hash_map:
            if hash_map[val] != -1:
                return hash_map[val]
            
        return -1 