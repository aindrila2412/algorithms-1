# 21. Merge Two Sorted Lists

"""
Merge two sorted linked lists and return it as a new sorted list. 
The new list should be made by splicing together the nodes of the first two lists.
"""
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # p = l1
#         q = l2 
#         s = None
            
#         if not p:
#             return q 
#         if not q:
#             return p
        
#         if p and q:
#             if p.val <= q.val:
#                 s = p
#                 p = s.next 
#             else:
#                 s = q 
#                 q = s.next
#             new_head = s 
        
#         while p and q:
#             if p.val <= q.val:
#                 s.next = p
#                 s = p 
#                 p = s.next 
#             else:
#                 s.next = q
#                 s = q
#                 q = s.next 
#         if not p:
#             s.next = q 
#         if not q:
#             s.next = p
#         return new_head


     # Using divide and conquer
        p = l1
        q = l2
        s = None 
        
        if not p:
            return q
        if not q:
            return p
        if p.val < q.val:
            p.next = self.mergeTwoLists(p.next, q)
            return p
        else:
            q.next = self.mergeTwoLists(p, q.next)
            return q
        
