# Shift the linked list by one element to the right
def move_tail_to_head(self):
    previous = None 
    current = self.head 
    while current.next:
        previous = current 
        current = current.next 
    current.next = self.head 
    self.head = previous.next
    previous.next = None 

    return self.head 