# Sorting an array using recursion 
def sort_insert(values, k):
    if len(values) == 0 or values[-1] <= k:
        values.append(k)
        return
    # Load the last element in a temporary variable
    temp = values[-1]
    # Pop the last element
    values.pop()
    # Recursively call the sort_insert method until induction is met
    sort_insert(values, k)
    # Add the temporary variable back to the next position
    values.append(temp)
    return
    
def sort_array(values):
    if len(values) == 1:
        return values
    k = values[-1]
    # Store the last index value in a temporary variable
    # sort_array(values[:-1])
    # Pop the last element from the value list 
    values.pop()
    # Recursively call the sort_array function with the updated value to sort the remaining array
    sort_array(values)
    # Insert the temporary variable into the array 
    sort_insert(values, k)

values = [10, 19, 110, 1, 3, 189, 10]
sort_array(values)
print(values)