# 567. Permutation in String
"""
    Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
    In other words, return true if one of s1's permutations is the substring of s2.

    Input: s1 = "ab", s2 = "eidbaooo"
    Output: true
    Explanation: s2 contains one permutation of s1 ("ba").
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash = [0] * 26
        s2_hash = [0] * 26
        
        # Base condition
        if len(s1) > len(s2):
            return False 
        
        left = 0
        right = 0
        # Fill up s1_hash and s2_hash upto length of s1 
        for i in range(len(s1)):
            s1_hash[ord(s1[i]) - ord('a')] += 1
            s2_hash[ord(s2[i]) - ord('a')] += 1
            # Increment the window end pointer
            right += 1
        right -= 1
        # Fill up s2_hash within the window of length len(s1)
        while right < len(s2):
            # If both the arrays are equal, return true
            if s1_hash == s2_hash:
                return True 
            # Increment the window by 1 to the right
            right += 1
            # Increment the count of the new element to the right side of the window 
            if right != len(s2):
                s2_hash[ord(s2[right]) - ord('a')] += 1
            # Remove the leftmost element as the window is shifted and we don't need it anymore
            s2_hash[ord(s2[left]) - ord('a')] -= 1
            # Decrement the window by 1 from the left 
            left += 1
        return False 
