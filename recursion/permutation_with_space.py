# Generate permutations with a space 
def permutation_with_space_helper(input_val, output_val):
    if len(input_val) == 0:
        # Base condition to get a final output once the input string is empty
        final.append(output_val)
        return 
    # Store the first element of the string and make decisions on it 
    temp = input_val[0]
    # Recursively calling the fnc including the temp in the output
    permutation_with_space_helper(input_val[1:], output_val + temp)
    # Recursively calling the fnc including the temp and "_" in the output
    permutation_with_space_helper(input_val[1:], output_val + "_" + temp)

def  permutation_with_space(input_val):
    output_val = ""
    # Calling the helper function
    for i in range(len(input_val)):
        permutation_with_space_helper(input_val[:i] + input_val[i+1:], input_val[i])

final = []
permutation_with_space('abc')
print(final)