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
    

def optimalCost(values):
    cost = 0
    new = MinHeap(values)
    check = 0 
    while len(new.values) > 1 or check == len(values) - 2:
        leftSide = new.pop()
        rightSide = new.pop()
        temp = (leftSide + rightSide)
        cost += temp
        new.push(temp)
        check += 1

    return cost

values = [1, 2, 3, 4, 5]
print(optimalCost(values))

