"""
    Given an array of integers and two numbers k1 and k2. 
    Find the sum of all elements between given two k1’th and k2’th smallest elements of the array. 
    It may  be assumed that all elements of array are distinct.

    Input: values = [10, 2, 50, 12, 48, 13], k1 = 2, k2 = 6 
    Output: 
"""
import heapq
class MinHeap:
    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = values 
            heapq.heapify(self.values)
    
    def push(self, value):
        heapq.heappush(self.values, value)
    
    def pop(self):
        return heapq.heappop(self.values)
    
    def top(self):
        return self.values[0]
    
def sumBetween(values, k1, k2):
    new = MinHeap(values)
    final = 0 
    a = heapq.nsmallest(k1, new.values)
    b = heapq.nsmallest(k2, new.values)
    for i, val in enumerate(values):
        if val > a[-1] and val < b[-1]:
            final += val
    return final



values = [10, 2, 50, 12, 48, 13]
k1 = 2
k2 = 6

print(sumBetween(values, k1, k2))