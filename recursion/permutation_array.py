# Creating all the permutation combinations of a given array of elements
def generate_permutations(final, values, index=0):
    if index == len(values):
        final.append(values.copy())
    else:
        # Looping over the array from the index element to the end 
        for i in range(index, len(values)):
            # Swapping the ith element to the index element
            values[index], values[i] = values[i], values[index]
            # Recursively updating the elements
            generate_permutations(final, values, index + 1)
            # Swapping the elements back to get back to the previous iteration
            values[index], values[i] = values[i], values[index]

final = []
generate_permutations(final, [1,2,3])
print(final)