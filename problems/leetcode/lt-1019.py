# 1019. Next Greater Node In Linked List
'''
    We are given a linked list with head as the first node.  Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

    Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val such that 
    j > i, node_j.val > node_i.val, and j is the smallest possible choice.  
    If such a j does not exist, the next larger value is 0.

    Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

    Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent the 
    serialization of a linked list with a head node value of 2, second node value of 1, and third node value of 5.

    Input: [1,7,5,1,9,2,5,1]
    Output: [7,9,9,9,0,5,0,0]
'''
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if not head:
            return head
        valueList = list()
        current = head 
        while current:
            valueList.append(current.val)
            current = current.next 
        stack = []
        finalList = [0] * len(valueList)
        
        # Looping with index, value
        for i, e in enumerate(valueList):
            # Check if the stack is not empty, 
            while stack and valueList[stack[-1]] < e:
                finalList[stack.pop()] = e
                
            stack.append(i)
        return finalList
        
        ##########################################
        # Solution in O(n^2)
        ##########################################
#         valueList = list()
#         finalList = list()
#         current = head
        
#         while current:
#             valueList.append(current.val)
#             current = current.next 
        
#         for i in range(len(valueList)):
#             check = 0
#             for j in range(i, len(valueList)):
#                 if valueList[j] > valueList[i]:
#                     check = valueList[j]
#                     break
#             finalList.append(check)
            
#         return finalList
                    