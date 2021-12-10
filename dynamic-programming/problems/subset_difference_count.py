# Count no of subsets with given difference
"""
    Narrow down the problem to a max sum as (diff + total) / 2 
    s2 - s1 = diff 
    s2 + s1 = total

    So, s1 = (total + diff) / 2
    and s2 = (total - diff) / 2
"""
def count_subsets_difference(arr, max_sum, length):
    # Create a table to store results of subproblems
    table = [[0 for i in range(max_sum + 1)] for j in range(length + 1)]
    for i in range(length + 1):
        for j in range(max_sum + 1):
            if i == 0:
                table[i][j] = 0
            if j == 0:
                table[i][j] = 1
    
    for i in range(1, length + 1):
        for j in range(1, max_sum + 1):
            if arr[i - 1] > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = table[i - 1][j] + table[i - 1][j - arr[i - 1]]
    return table[length][max_sum]

arr = [1, 1, 2, 3]
difference = 1 
max_sum = ((difference + sum(arr)) // 2)
count_number = count_subsets_difference(arr, max_sum, len(arr))
print(count_number)
