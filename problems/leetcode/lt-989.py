# 989. Add to Array-Form of Integer
"""
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.
For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.
"""
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        # Initialise sum as 0
        value_sum = 0
        # Initialise the final array as empty array
        new_arr = []
        a_len = len(A) - 1

        # If the A array is a single index array, make the sum equal to that index value 
        if len(A) < 2:
            value_sum = A[0]
        else:
            # Otherwise, loop over and append the array values into a single integer value
            for i in range(len(A)):
                value_sum += A[i] * pow(10, a_len - i)
        # Add the two integers 
        value_sum += K 
        # If, the final sum is 0, return it
        if value_sum == 0:
            return [0]

        # Append the values to the new array
        while value_sum > 0:
            remainder = value_sum % 10 
            new_arr.append(remainder)
            value_sum = value_sum // 10 
        # Reverse the array and return it 
        return new_arr[::-1]
            