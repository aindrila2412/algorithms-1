# 23. Merge k Sorted Lists
"""
    You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list and return it.
    
    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # METHOD 1: Using Merge sort 
        # Time Complexity: O(n logn)
        # Space Complexity: O(n)
        # Method to merge sort 
        def merge_sort(unsorted_list):
            def merge_list(leftSide, rightSide):
                sorted_array = []
                while leftSide and rightSide:
                    sorted_array.append((leftSide if leftSide[0] <= rightSide[0] else rightSide).pop(0))
                return sorted_array + leftSide + rightSide
            if len(unsorted_list) <= 1:
                return unsorted_list
            mid_term = len(unsorted_list) // 2
            return merge_list(merge_sort(unsorted_list[:mid_term]), merge_sort(unsorted_list[mid_term:]))
                
        # Create a new list with all the items 
        new_list = list()
        
        # Getting the values from the linked lists 
        for i in range(len(lists)):
            current = lists[i]
            
            while current:
                new_list.append(current.val)
                current = current.next 
        
        new_list = merge_sort(new_list)
        if len(new_list) > 0:
            final_list = ListNode(val=new_list[0], next=None)
            current = final_list
            for i in range(1, len(new_list)):
                current.next = ListNode(val=new_list[i], next=None)
                current = current.next 

            return final_list
        else:
            return ListNode(val="")

        # METHOD 2: Using a priority queue 
        # Time Complexity: O(n log k)
        # Space complexity: O(n)
        # Iterate over each list and add it to the priority queue
        new_list = list()
        for i in lists:
            current = i
            while current:
                heapq.heappush(new_list, current.val)
                current = current.next
        if len(new_list) > 0:
            final_list = ListNode(heapq.heappop(new_list))
            current = final_list
            for i in range(len(new_list)):
                temp = heapq.heappop(new_list)
                current.next = ListNode(temp)
                current = current.next
            return final_list
        else:
            return ListNode("")