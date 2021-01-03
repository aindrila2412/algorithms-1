# 69. Sqrt(x)
"""
    Given a non-negative integer x, compute and return the square root of x.
    Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

    The below method uses Newton Square root method
"""
class Solution:
    # Define the function to call square root of a number
    def mySqrt(self, x: int) -> int:
        # Using newton square root method 
        return self.squareIteration(1.0, x)
    
    # Find the square roor using a guess and the value
    def squareIteration(self, guess, x):
        while self.goodEnough(guess, x) != True:
            guess = self.guessImprove(guess, x)
        return int(guess)
    
    # Check if the guess is close to the exact square root
    def goodEnough(self, guess, x):
        return (abs(self.square(guess) - x) < 0.001)
    
    # Method to find the square of two numbers 
    def square(self, value):
        return (value*value)
    
    # If a guess is not the square root, improve it
    def guessImprove(self, guess, x):
        return self.average(guess, (x/guess))
    
    # Function to find the average of 2 numbers
    def average(self, x, y):
        return (x + y) / 2
    
        