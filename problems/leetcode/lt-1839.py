# 1839. Longest Substring Of All Vowels in Order
"""
    A string is considered beautiful if it satisfies the following conditions:

        - Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
        - The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).
        - For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are not beautiful.

    Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no such substring exists, return 0.

    A substring is a contiguous sequence of characters in a string.

    Input: word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
    Output: 13
    Explanation: The longest beautiful substring in word is "aaaaeiiiiouuu" of length 13.
"""

class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        max_length = 0
        # Handle edge case
        if len(word) == 1:
            return 0
        
        ptr1 = 0 
        ptr2 = 1
        curr = set(word[0])x
        
        while ptr2 < len(word):
            if ord(word[ptr2 - 1]) <= ord(word[ptr2]):
                curr.add(word[ptr2])
                if len(curr) == 5:
                    max_length = max(max_length, ptr2 - ptr1 + 1)
            else:
                # Create the previous pointer as next pointer
                ptr1 = ptr2
                curr = set(word[ptr1])
            # Increment the next pointer by 1 
            ptr2 += 1
        return max_length