# 142. Linked List Cycle II
"""
    Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

    Notice that you should not modify the linked list.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Using Floyd Cycle Detection
        prev = head
        current = head 
        check = 0
        while current and current.next:
            prev = prev.next 
            current = current.next.next 
            if prev == current:
                check = 1
                break 
        if check == 0:
            return None
        else:
            prev = head
            while prev != current:
                prev = prev.next 
                current = current.next 

            return current 
            
            
        