# 66. Plus One
"""
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Input: [9,9,9]
Output: [1,0,0,0]
"""
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1 , -1, -1):
            element = digits[i] + carry 
            if element > 9:
                digits[i] = element % 10
                carry = 1
            else:
                digits[i] = element
                carry = 0
        if carry == 1:
            digits = [1] + digits
        return digits
                
