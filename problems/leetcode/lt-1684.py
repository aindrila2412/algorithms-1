# 1684. Count the Number of Consistent Strings
"""
    You are given a string allowed consisting of distinct characters and an array of strings words. 
    A string is consistent if all characters in the string appear in the string allowed.
    Return the number of consistent strings in the array words.

    Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
    Output: 2
    Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
"""
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Method 1 -> Takes lesser run time using sets 
        allowed_set = set(allowed)
        count = 0
        for word in words:
            word = set(word)
            if word == allowed_set or word.issubset(allowed_set):
                count += 1
        return count
        
        # Method 2 -> Takes more run time 
        count = 0
        for word in words:
            ctr = 0
            for char in word:
                if char not in allowed:
                    ctr = -1
                    break 
            if ctr == 0:
                count += 1
        return count
