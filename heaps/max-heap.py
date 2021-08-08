"""
    1. Create a max heap
    2. Insert into the max heap
    3. Heapify the max heap upwards 
    4. Heapify the max heap downwards
    5. Delete from the max-heap 
"""
class MaxHeap:
    def __init__(self, capacity):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0
    
    def get_parent_index(self, index: int):
        return (index - 1) // 2

    def get_left_child_index(self, index: int):
        return (2 * index) + 1 

    def get_right_child_index(self, index: int):
        return (2 * index) + 2 
    
    def check_for_parent_presence(self, index: int):
        return self.get_parent_index(index) >= 0
    
    def check_for_left_child_presence(self, index: int):
        return self.get_left_child_index(index) < self.size 

    def check_for_right_child_presence(self, index: int):
        return self.get_right_child_index(index) < self.size 

    def is_full(self):
        return self.size == self.capacity
    
    def get_parent_value(self, index: int):
        return self.storage[self.get_parent_index(index)]
    
    def get_left_child_value(self, index: int):
        return self.storage[self.get_left_child_index(index)]

    def get_right_child_value(self, index: int):
        return self.storage[self.get_right_child_index(index)]
    
    def swap_indexes(self, index_1, index_2):
        temp = self.storage[index_1]
        self.storage[index_1] = self.storage[index_2]
        self.storage[index_2] = temp

    def heapifyUp_iterative(self):
        index = self.size - 1 
        while (self.get_parent_value(index) and self.get_parent_value(index) < self.storage[index]):
            self.swap_indexes(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def heapifyUp_recursive(self, index):
        if self.get_parent_value(index) and self.get_parent_value(index) < self.storage[index]:
            self.swap_indexes(self.get_parent_index(index), index)
            self.heapifyUp_recursive(self.get_parent_index(index))

    def heapifyDown_iterative(self):
        index = 0
        while self.check_for_left_child_presence(index):
            greater_child_index = self.get_left_child_index(index)
            if self.check_for_right_child_presence(index) and self.get_right_child_value(index) > self.get_left_child_value(index):
                greater_child_index = self.get_right_child_index(index)
            if self.storage[index] > self.storage[greater_child_index]:
                break
            else:
                self.swap_indexes(index, greater_child_index)
            index = greater_child_index

    def heapifyDown_recursive(self, index):
        greater_child_index = index
        if self.check_for_left_child_presence(index) and self.get_left_child_value(index) > self.storage[greater_child_index]:
            greater_child_index = self.get_left_child_index(index)
        if self.check_for_right_child_presence(index) and self.get_right_child_value(index) > self.storage[greater_child_index]:
            greater_child_index = self.get_right_child_index(index)
        if greater_child_index != index:
            self.swap_indexes(index, greater_child_index)
            self.heapifyDown_recursive(greater_child_index)

    def insert_iterative(self, data: int):
        if self.is_full():
            raise ('Heap is already full')
        else:
            self.storage[self.size] = data 
            self.size += 1
            self.heapifyUp_iterative()

    def insert_recursive(self, data: int):
        if self.is_full():
            raise ('Heap is already full')
        else:
            self.storage[self.size] = data 
            self.size += 1
            self.heapifyUp_recursive(self.size - 1)
    
    def remove_max_iterative(self):
        if self.size == 0:
            raise ('Heap is empty!')
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown_iterative()
        return data

    def remove_max_recursive(self):
        if self.size == 0:
            raise ('Heap is empty!')
        else:
            data = self.storage[0]
            self.storage[0] = self.storage[self.size - 1]
            self.size -= 1
            self.heapifyDown_recursive(0)
            return data

    def delete_element(self, index):
        if self.size == 0:
            raise('Heap is empty!')
        data = self.storage[index]
        self.storage[index] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyUp_recursive(index)
        self.heapifyDown_recursive(0)
        return data

    def print_heap(self):
        print(self.storage)



x = MaxHeap(10)
x.insert_recursive(1)
x.insert_recursive(10)
x.insert_recursive(3)
x.insert_recursive(5)
x.insert_recursive(2)
x.insert_recursive(4)
x.insert_recursive(0)
x.print_heap()
print(x.size)
x.remove_max_recursive()
x.print_heap()
print(x.size)
x.delete_element(4)
x.print_heap()