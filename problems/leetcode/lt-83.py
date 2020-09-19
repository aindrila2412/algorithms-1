# 83. Remove Duplicates from Sorted List

"""
Given a sorted linked list, delete all duplicates such that each element appear only once.
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
#         current = head 
#         previous = None 
#         check_values = {}
#         while current:
#             if current.val in check_values:
#                 previous.next = current.next
#                 current = None 
#             else:
#                 check_values[current.val] = 1 
#                 previous = current 
#             current = previous.next
#         return head
        if not head:
            return head
        current = head 
        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head