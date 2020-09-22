# 206. Reverse Linked List
"""
Reverse a singly linked list.

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # def _reverse(current, previous):
        #     if not current:
        #         return previous
        #     nxt = current.next 
        #     current.next = previous
        #     previous = current 
        #     current = nxt
        #     return _reverse(current, previous)
        # head = _reverse(current=head, previous=None)
        # return head
        
        previous = None 
        current = head 
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt
        head = previous
        return head

    
    

        
        