# Creating all the permutation combinations of a given string
def gen_permutations(values, left, right = ""):
    if len(left) == 0:
        values.append(right)
    else:
        for i in range(len(left)):
            gen_permutations(values, left[:i] + left[i+1:], right + left[i])

values = []
gen_permutations(values, 'abcd')
print(values)