# 445. Add Two Numbers II
'''
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = list()
        stack2 = list()
        
        while l1:
            stack1.append(l1.val)
            l1 = l1.next 
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next 
        
        carryValue = 0
        new_next = None
        while stack1 != [] or stack2 != []:
            sums = carryValue
            
            if stack1 != []:
                sums += stack1.pop()
             
            if stack2 != []:
                sums += stack2.pop()
            carryValue = sums // 10
    
            if sums >= 10:
                carryValue = 1
                remainder = sums % 10
                new_next = ListNode(remainder, new_next)
                
            else:
                carryValue = 0
                new_next = ListNode(sums, new_next)
                
        if carryValue == 1:
            new_next = ListNode(1, new_next)
            
        return new_next
            