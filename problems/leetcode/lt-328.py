# 328. Odd Even Linked List
'''
	Given a singly linked list, group all odd nodes together followed by the even nodes. 
	Please note here we are talking about the node number and not the value in the nodes.
	You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

	Input: 2->1->3->5->6->4->7->NULL
    Output: 2->3->6->7->1->5->4->NULL
'''
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
    	# If the linked list is empty
        if not head:
            return head
        # Make two seperate lists, skipping each node as even and odd
        oddNodes = head
        evenNodes = head.next 
        evenHead = evenNodes 
        
        while (evenNodes and oddNodes and evenNodes.next and oddNodes.next):
            oddNodes.next = evenNodes.next 
            oddNodes = oddNodes.next 
            evenNodes.next = oddNodes.next 
            evenNodes = evenNodes.next 
        oddNodes.next = evenHead 
        return head