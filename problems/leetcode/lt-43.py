# 43. Multiply Strings
"""
Given two non-negative integers num1 and num2 represented as strings, 
return the product of num1 and num2, also represented as a string.

Input: num1 = "123", num2 = "456"
Output: "56088"
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        checkDict = {"0": 0,"1":1 ,"2":2 ,"3": 3,"4": 4,"5":5 ,"6": 6,"7": 7,"8":8,"9":9 }    
        def convert_str_to_int(numString):
            value = 0 
            for i, val in enumerate(numString):
                value += 10 ** (len(numString) - (i + 1)) * checkDict[val]
            return value 
        
        def convert_int_to_str(numInt):
            # convert checkDict from key:value to value:key
            newDict = { value:key for key, value in checkDict.items() }
            # Returns: {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
            finalString = ""
            while numInt > 0:
                finalString = newDict[numInt % 10] + finalString
                numInt = numInt // 10
            return finalString
    
        if num1 == '0' or num2 == '0':
            return '0'
        # Multiplication could be donw using Karatsuba multiplication for the most optimised solution
        return convert_int_to_str(convert_str_to_int(num1) * convert_str_to_int(num2))
        
        
        