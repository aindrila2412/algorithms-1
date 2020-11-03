# 415. Add Strings
"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # Not using inbuilt functions to convert strings into integer and vice versa,
        # instead using ord() and chr() to do the job.
        int_1 = 0 
        int_2 = 0
        # Loop over and convert the string into an integer using ord()
        for i in range(len(num1)):
            # Subtract the ascii value of 48 from the ascii of all characters
            value = ord(num1[i]) - ord('0')
            int_1 += value * pow(10, len(num1) - 1 - i)
        for i in range(len(num2)):
            # Subtract the ascii value of 48 from the ascii of all characters
            value = ord(num2[i]) - ord('0')
            int_2 += value * pow(10, len(num2) - 1 - i)
            
        # Adding the values to get the sum
        final_sum = int_1 + int_2 
        # Convert integer to string  
        final_string = ""

        # If the final sum is 0, just return the character 0 
        if final_sum == 0:
            return chr(ord('0'))

        # Loop over and append the integer characters to the string 
        while final_sum > 0:
            remainder = final_sum % 10 
            value = remainder + ord('0')
            final_string += chr(value)
            final_sum = final_sum // 10

        # Return the reversed string
        return final_string[::-1]
            
        