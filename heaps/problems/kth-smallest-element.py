# Find the k-th smallest element 
"""
    Input: [8, 11, 5, 4, 21, 16], k = 3
    Output: 8
"""
import heapq 
class MaxHeap:
    def __init__(self, values=None):
        if values is None:
            self.values = []
        else:
            self.values = [-val for val in values]
            heapq.heapify(self.values)
    
    def push(self, value):
        heapq.heappush(self.values, -value)

    def pop(self):
        return -heapq.heappop(self.values)

    def top(self):
        return -self.values[0]
    
    def replace(self, value):
        return heapq.heapreplace(self.values, -value)

def k_smallest_element(values, k):
    new = MaxHeap(values[0:k])

    for i in range(k, len(values)):
        if values[i] < new.top():
            new.replace(values[i])
    
    return new.top()

values = [8, 11, 5, 4, 21, 16]
k = 3
print(k_smallest_element(values, k))
