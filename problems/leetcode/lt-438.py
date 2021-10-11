# 438. Find All Anagrams in a String
"""
    Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Initialise the two hash arrays
        s1_hash = [0] * 26
        s2_hash = [0] * 26
        # Final list to return
        final = []
        left, right = 0, 0

        # Edge case
        if len(s) < len(p):
            return final
        
        # Fill up the s1_hash and s2_hash upto the length of p array
        for i in range(len(p)):
            s1_hash[ord(p[i]) - ord('a')] += 1
            s2_hash[ord(s[i]) - ord('a')] += 1
            # Increment the window end pointer
            right += 1
        right -= 1
        
        # Fill up the s2_hash within the slidign window of length of length s
        while right < len(s):
            # If both hash arrays are equal, append the starting index
            if s1_hash == s2_hash:
                final.append(left)
            # Increment the window by 1 to the right
            right += 1
            # Increment the count of the new element to the right side of the window 
            if right != len(s):
                s2_hash[ord(s[right]) - ord('a')] += 1
            
            # Remove the leftmost element as the window is shifted and we don't need it anymore
            s2_hash[ord(s[left]) - ord('a')] -= 1
            # Decrement the window by 1 from the left 
            left += 1
            
        return final 
            
            