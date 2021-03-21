# 1769. Minimum Number of Operations to Move All Balls to Each Box
"""
    You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box 
    is empty, and '1' if it contains one ball.

    In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j 
    if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

    Return an array answer of size n, where answer[i] is the minimum number of operations needed to move 
    all the balls to the ith box.

    Each answer[i] is calculated considering the initial state of the boxes.   

    Input: boxes = "001011"
    Output: [11,8,5,4,3,4] 
"""
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        output = [0] * len(boxes)
        count_left = 0
        count_right = 0
        left_value = 0
        right_value = 0
        
        """
            Increment the left count value by 1 if i-1 is equal to '1'
            Increment the left count with the value of left count value on each index to the right
        """
        for i in range(1, len(boxes)):
            if boxes[i - 1] == '1':
                count_left += 1 
            left_value += count_left 
            output[i] = left_value 
            
        """
            Increment the right count value by 1 if i+1 is equal to '1'
            Increment the right count with the value of right count value on each index to the left
        """
        for i in range(len(boxes) - 2, -1, -1):
            if boxes[i + 1] == '1':
                count_right += 1
            right_value += count_right 
            output[i] += right_value 
            
        return output
        