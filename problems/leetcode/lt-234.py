# 234. Palindrome Linked List
"""
Given a singly linked list, determine if it is a palindrome.

Input: 1->2
Output: false
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        stack = []
        current = head 
        while current:
            stack.append(current.val)
            current = current.next 
        current = head
        while current:
            data = stack.pop()
            if data != current.val:
                return False
            current = current.next 
        return True
