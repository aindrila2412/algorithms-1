# 203. Remove Linked List Elements
"""
Remove all elements from a linked list of integers that have value val.

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
"""

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
#         Method 1 using a dummy head        
#         check = ListNode(0, head)
#         check.next = head
#         current = check
#         if not head:
#             return None

#         while current and current.next:
#             if current.next.val == val:
#                 current.next = current.next.next
#             else:
#                 current = current.next
        # return check.next

# Method 2 takes less running time 
        if not head:
            None 
        current = head 
        previous = head 
        
        while current:
            if current.val == val:
                previous.next = current.next
                if head.val == val:
                    head = head.next 
            else:
                previous = current 
            current = current.next
        return head
