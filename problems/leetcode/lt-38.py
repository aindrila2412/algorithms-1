# 38. Count and Say
"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read 
as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", 
so the answer is the concatenation of "12" and "11" which is "1211".
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        # Helper function to return the string for n-th iteration
        def countAndSay_helper(s):
            result = []
            i = 0
            while i < len(s):
                count = 1
                while i+1 < len(s) and s[i] == s[i+1]:
                    count += 1
                    i += 1
                result.append(str(count) + s[i])
                i += 1
            return "".join(result)

        s = "1"
        for i in range(n - 1):
            s = countAndSay_helper(s)
        return s
            
            