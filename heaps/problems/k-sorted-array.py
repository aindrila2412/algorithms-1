# Sort k sorted array 
"""
    values = [6, 5, 3, 2, 8, 10, 9]
    k = 4
    Output: [2, 3, 5, 6, 8, 9, 10]
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


def kSortedArray(values, k):
    new = MinHeap(values[0:k])
    index = 0
    values[index] = new.top()

    for i in range(k, len(values)):
        index += 1 
        new.replace(values[i])
        values[index] = new.top()

    while len(new.values) > 0:
        values[index] = new.top()
        new.pop()
        index += 1
    
    return values 

values = [6, 5, 3, 2, 8, 10, 9]
k = 4 
print(kSortedArray(values, k))