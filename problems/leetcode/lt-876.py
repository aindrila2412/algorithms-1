# 876. Middle of the Linked List
"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head.next == None:
            return head
        # arr = []
        # count = 0
        # while head != None:
        #     count += 1
        #     arr.append(head)
        #     head = head.next
        # return arr[len(arr) // 2]
        curr = head
        count = 0
        while head != None:
            count += 1
            head = head.next
        for _ in range(count // 2):
            curr = curr.next 
        return curr
        
            