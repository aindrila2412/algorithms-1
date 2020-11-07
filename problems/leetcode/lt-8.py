# 8. String to Integer (atoi)
"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
Then, starting from this character takes an optional initial plus or minus sign followed by as 
many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, 
which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, 
or if no such sequence exists because either str is empty or it contains only whitespace characters, 
no conversion is performed.
If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered a whitespace character.
Assume we are dealing with an environment that could only store integers within the 32-bit signed 
integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, 
INT_MAX (231 − 1) or INT_MIN (−231) is returned.
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        # Remove whitespaces 
        s = s.strip()
        
        # Length of the string for conversion 
        s_len = len(s)
        
        # Initialise final integer value as 0
        value = 0
        
        # Initialise the sign counter 
        sign_counter = 0 
        
        # Initialise isNegative as False 
        isNegative = False 
        
        # Loop over and convert the string into integer using ord()
        for i in range(len(s)):
            # Check for a negative sign
            if i == 0 and s[i] == '-':
                isNegative = True 
                # Decrement the value of the string length
                s_len -= 1
                if sign_counter == 1:
                    return 0
                sign_counter += 1
                
            # Check for a positive sign
            elif i == 0 and s[i] == "+":
                # Decrement the string of the string length 
                s_len -= 1
                if sign_counter == 1:
                    return 0
                sign_counter += 1 
            
            # If the character is not an integer or -/+
            elif s[i].isdigit() == False:
                break 
                
            else:
                current = ord(s[i]) - ord('0')
                value = (value * 10) + current
                s_len -= 1
                
        # Check if the output is not a 32-bit signed integer 
        if value > 2 ** 31 - 1 or value < -2 * 31:
            if isNegative:
                return -2 ** 31 
            else:
                return 2 ** 31 - 1
                
        # Check if the value was negative, return the negative integer
        if isNegative:
            return -1 * value 
        return value 
                
                
                