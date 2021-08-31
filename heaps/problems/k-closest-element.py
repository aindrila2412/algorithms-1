# Find K Closest Elements

import heapq 

class MaxHeap:
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

    def replace(self, val):
        heapq.heapreplace(self.values, val)

def kClosestElements(values, k, x):
    arr = MaxHeap()
    final = []
    
    for i, val in enumerate(values):
        temp = abs(val - x)
        if len(arr.values) > k - 1 and arr.top()[0] < -temp: 
            arr.replace((-temp, val))
        elif len(arr.values) < k:
            arr.push((-temp, val))
    

    while len(arr.values) > 0:
        print(arr.values)
        temp = arr.pop()
        final.append(temp[1])
    return sorted(final)

values = [1,2]
k = 1
x = 1
print(kClosestElements(values, k, x))



