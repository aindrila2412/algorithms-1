# 242. Valid Anagram
"""
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    Input: s = "anagram", t = "nagaram"
    Output: true
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        return dict(Counter(s)) == dict(Counter(t))