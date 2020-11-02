# 2. Add Two Numbers
"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack_l1 = list()
        stack_l2 = list()
        
        # Append the values of l1 to the stack_l1
        while l1:
            stack_l1.append(l1.val)
            l1 = l1.next 
            
        # Append the values of l2 to the stack_l2
        while l2:
            stack_l2.append(l2.val)
            l2 = l2.next 
            
        # Initialise carry value 
        carry = 0 
        new_list = []
        new_link = None
        
        while stack_l1 != [] or stack_l2 != []:
            # Initialise sum as 0 on each iteration
            sums = carry 
            
            if stack_l1 != []:
                sums += stack_l1.pop(0)
            
            if stack_l2 != []:
                sums += stack_l2.pop(0)
                
            carry = sums // 10
                
            if sums > 9:
                carry = 1 
                remainder = sums % 10
                new_list.append(remainder)
                
            else:
                carry = 0
                new_list.append(sums)
                
        # If carry value is still 1
        if carry == 1:
            new_list.append(1)
            
        # Loop over the new list and create the new linked list
        while new_list != []:
            value = new_list.pop()
            new_link = ListNode(value, new_link)
            
        return new_link