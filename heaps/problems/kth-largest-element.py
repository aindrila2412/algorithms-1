# Kth largest element in the list 
"""
    values = [7, 10, 4, 3, 20, 15]
    k = 3 
    Output: 10
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

    def replace(self, value):
        return heapq.heapreplace(self.values, value)

def findKLargest(values, k):
    new = MinHeap(values[0:k])

    for i in range(k, len(values)):
        if values[i] > new.top():
            new.replace(values[i])
    
    return new.top()


values = [7, 10, 4, 3, 20, 15]
k = 4 
print(findKLargest(values, k))