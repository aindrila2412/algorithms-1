# 1370. Increasing Decreasing String
"""
    Given a string s. You should re-order the string using the following algorithm:
        1) Pick the smallest character from s and append it to the result.
        2) Pick the smallest character from s which is greater than the last appended character to the result and append it.
        3) Repeat step 2 until you cannot pick more characters.
        4) Pick the largest character from s and append it to the result.
        5) Pick the largest character from s which is smaller than the last appended character to the result and append it.
        6) Repeat step 5 until you cannot pick more characters.
        7) Repeat the steps from 1 to 6 until you pick all characters from s.

    In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.
    Return the result string after sorting s with this algorithm.

    Input: s = "aaaabbbbcccc"
    Output: "abccbaabccba"
    Explanation: After steps 1, 2 and 3 of the first iteration, result = "abc"
    After steps 4, 5 and 6 of the first iteration, result = "abccba"
    First iteration is done. Now s = "aabbcc" and we go back to step 1
    After steps 1, 2 and 3 of the second iteration, result = "abccbaabc"
    After steps 4, 5 and 6 of the second iteration, result = "abccbaabccba"
"""
from collections import Counter
class Solution:
    def sortString(self, s: str) -> str:
        value_count = Counter(s)
        final = ""
        flag = 0 
        
        for i in range(value_count.most_common(1)[0][1]):
            if flag == 0:
                for j in range(97, 123):
                    if chr(j) in value_count and value_count[chr(j)] > 0:
                        final = final + chr(j)
                        value_count[chr(j)] -= 1
                flag = 1 
            elif flag == 1:
                for j in range(122, 96, -1):
                    if chr(j) in value_count and value_count[chr(j)] > 0:
                        final = final + chr(j)
                        value_count[chr(j)] -= 1
                flag = 0
                
        return final 
                
            
        
        