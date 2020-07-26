# 24. Swap Nodes in Pairs

'''
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Input: 1->2->3->4,
Output: 2->1->4->3.
'''
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        current = head 
        while current:
            if current.next == None:
                return head
            if current.next:
                current.val, current.next.val = current.next.val, current.val
            current = current.next.next
        return head