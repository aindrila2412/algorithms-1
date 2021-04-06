"""
    Given the head of a singly linked list, return true if it is a palindrome.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = list()
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        
        end = len(arr) - 1
        
        for i in range(0, len(arr) // 2):
            if arr[i] != arr[end]:
                return False 
            end -= 1
            
        return True