# 28. Implement strStr(
"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

"""
# THis could be implemented using inbuilt python functions, but I have used KMP algorithm to do so
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Taking the edge cases 
        if len(needle) == 0:
            return 0
        
        # Helper method to get the array for the pattern to match based on the failure function 
        def getArray(substring, test_array):
            substring_len = len(substring)
            i = 0 
            j = 1 
            
            # global test_array 
            test_array[0] = 0 
            # Loop over till the second pointer reaches the end of the array 
            while j < substring_len:
                if substring[i] == substring[j]:
                    i = i + 1 
                    test_array[j] = i 
                    j = j + 1 
                # If the first character didn't matched 
                elif i == 0:
                    test_array[j] = 0
                    j = j + 1 
                # Mismatch after at least one matching character 
                else:
                    i = test_array[i - 1]
            return test_array
        # Implementing Knuth Morris Pratt Algorithm 
        def kmp(substring, text, test_array):
            i = 0
            j = 0 
            key = -1
            # 
            while i < len(substring) and j < len(text):
                if substring[i] == text[j] and i == len(substring) - 1:
                    # Return the start index of the matched substring in the text
                    return j - len(substring) + 1
                # Character matches:
                elif substring[i] == text[j]:
                    i = i + 1 
                    j = j + 1 
                # Character didn't match -> Backtrack:
                else:
                    if i != 0:
                        i = test_array[i - 1]
                    else:
                        j = j + 1 
                        
            return -1 
        
        test_array = [None] * len(needle)
        test = getArray(needle, test_array)
        x = kmp(needle, haystack, test)
        return x