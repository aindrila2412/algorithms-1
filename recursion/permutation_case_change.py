# Generate all permutations of a string by changing case of the characters as well
"""
    Input: 'abc'
    Output: ['abc', 'abC', 'aBc', 'aBC', 'Abc', 'AbC', 'ABc', 'ABC']
"""
# Helper method to compute the resulting array of permutations
def permutation_case_change_helper(input_val, output_val):
    # Base condition to return when input string is empty
    if len(input_val) == 0:
        final.append(output_val)
        return
    
    # Store the first element of the string and make decisions on it 
    temp = input_val[0]
    # Recursively calling the function with the lowercase input (temp)
    permutation_case_change_helper(input_val[1:], output_val + temp)
    # Recursively calling the function with the uppercase input (temp)
    permutation_case_change_helper(input_val[1:], output_val + temp.upper())

def permutation_case_change(input_val):
    for i in range(len(input_val)):
        # Recursively calling the helper function with the lowercase input string
        permutation_case_change_helper(input_val[:i] + input_val[i+1:], input_val[i])
        # Recursively calling the helper function with the uppercase input string
        permutation_case_change_helper(input_val[:i] + input_val[i+1:], input_val[i].upper())

final = list()
permutation_case_change('abc')
print(final)