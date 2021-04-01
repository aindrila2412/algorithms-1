# 717. 1-bit and 2-bit Characters
"""
    We have two special characters. The first character can be represented by one bit 0. 
    The second character can be represented by two bits (10 or 11).
    Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. 
    The given string will always end with a zero.

    Input: 
    bits = [1, 0, 0]
    Output: True
    Explanation: 
    The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
"""
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        index = 0 
        # If a "1" bit is encountered, it assumes there is a 0 or 1 bit after it
        # So, appending the value of index counter by the value + 1
        while index < len(bits) - 1:
            index += bits[index] + 1
        return index == len(bits) - 1
        