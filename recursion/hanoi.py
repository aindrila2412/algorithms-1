# Tower of Hanoi using recursion 
def tower_of_hanoi(n, source, destination, helper):
    # Base condition to move the lase element in the source bar to the destintion bar
    if n == 1:
        status(n, source, destination)
        return
    # Recursively reducing the disks, and pushing it to the helper bar
    tower_of_hanoi(n - 1, source, helper, destination)
    status(n, source, destination)
    # Recursively reducing the disks and pushing it to the destination bar 
    tower_of_hanoi(n - 1, helper, destination, source)
    
# Helper method to print the transition
def status(n, source, destination):
    print('Moving disk {} from {} to {}'.format(n, source, destination))

tower_of_hanoi(3, 1, 3, 2)
