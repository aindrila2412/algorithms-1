'''
    1. Create a min heap
    2. Insert into the min heap
    3. Heapify the min heap

'''
class MinHeap:
    def __init__(self, capacity: int) -> None:
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0
    
    def get_parent_index(self, index: int) -> int:
        # Parent index is equal to floor((index - 1) / 2)
        return (index - 1) // 2

    def get_left_child_index(self, index: int) -> int:
        return (2 * index) + 1
    
    def get_right_child_index(self, index: int) -> int:
        return (2 * index) + 2

    def check_for_parent_presence(self, index: int) -> bool:
        return self.get_left_child_index(index) >= 0
    
    def check_for_left_child_presence(self, index: int) -> bool:
        return self.get_left_child_index < self.size 
    
    def check_for_right_child_presence(self, index: int) -> bool:
        return self.get_right_child_index < self.size

    def get_parent_value(self, index: int):
        return self.storage[self.get_parent_index(index)]
    
    def get_left_child_value(self, index: int):
        return self.storage[self.get_left_child_index(index)]

    def get_right_child_value(self, index: int):
        return self.storage[self.get_right_child_index(index)]

    def is_full(self) -> bool:
        return self.size == self.capacity

    def swap_indexes(self, index_1, index_2):
        temp = self.storage[index_1]
        self.storage[index_1] = self.storage[index_2]
        self.storage[index_2] = temp

    def heapifyUp_iterative(self):
        index = self.size - 1 
        # Loop over and keep going up the tree
        while (self.check_for_parent_presence(index) and self.get_parent_value(index) > self.storage[index]):
            # Until, keep swapping the two indices 
            self.swap_indexes(self.get_parent_index(index), index)
            # Make the swapped parent index as the current index
            index = self.get_parent_index(index)

    def heapifyUp_recursive(self, index):
        if self.check_for_parent_presence(index) and self.get_parent_value(index) > self.storage[index]:
            self.swap_indexes(self.get_parent_index(index), index)
            self.heapifyUp_recursive(self.get_parent_index(index))

    def insert_iterative(self, data):
        if self.is_full():
            raise ('Heap is already full')
        else:
            self.storage[self.size] = data 
            self.size += 1
            # Once inserted at the end, we need to heapify our entire heap 
            self.heapifyUp_iterative()
    
    def insert_recursive(self, data):
        if self.is_full():
            raise ('Heap is already full')
        else:
            self.storage[self.size] = data
            self.size += 1
            self.heapifyUp_recursive(self.size - 1)

    def remove_min(self):
        # Handle edge case
        if len(self.size) == 0:
            raise ('Heap is empty!')
        else:
            data = self.storage[0]

    
    def print_heap(self):
        print(self.storage)    



x = MinHeap(10)
x.insert_recursive(1)
x.insert_recursive(10)
x.insert_recursive(3)
x.insert_recursive(5)
x.insert_recursive(2)
x.insert_recursive(4)
x.insert_recursive(0)
x.print_heap()
