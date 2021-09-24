# Reverse an array using recursion using O(1) space 
def reverse_insert(values, k):
    # Base condition to check for empty array
    if len(values) == 0:
        values.append(k)
        return
    # Pop out the last element and store it
    temp = values[-1]
    values.pop()
    # Recursive call with the updated function
    reverse_insert(values, k)
    # Append the remaining left out value
    values.append(temp)
    return

def reverse_array(values):
    # Base condition when array has just 1 value left 
    if len(values) == 1:
        return values
    # Pop out the last element and store it
    k = values[-1]
    values.pop()
    # Recursive call with the updated array
    reverse_array(values)
    # Induction step to make another call to the recursive function to insert the left out value
    reverse_insert(values, k)

values = [5,4,3,2,1]
reverse_array(values)
print(values)