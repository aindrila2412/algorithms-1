def subset_sum_recursive(values, max_sum, length):
    if max_sum == 0:
        return True

    if length == 0:
        return False
    
    if values[-1] <= max_sum:
        return subset_sum_recursive(values[:-1], max_sum - values[-1], length - 1) or subset_sum_recursive(values[:-1], max_sum, length - 1)
        
    if values[-1] > max_sum:
        return subset_sum_recursive(values[:-1], max_sum, length - 1)


def subset_sum_memoization(values, max_sum, length):
    if max_sum == 0:
        return True

    if length == 0:
        return False

    if dp[length][max_sum] != -1:
        return dp[length][max_sum]

    if values[-1] <= max_sum:
        dp[length][max_sum] = subset_sum_memoization(values[:-1], max_sum - values[-1], length - 1) or subset_sum_memoization(values[:-1], max_sum, length - 1)
        return dp[length][max_sum]

    if values[-1] > max_sum:
        dp[length][max_sum] = subset_sum_memoization(values[:-1], max_sum, length - 1)
        return dp[length][max_sum]

def subset_sum_top_down(values, max_sum, length):
    for i in range(length + 1):
        for j in range(max_sum + 1):
            if i == 0:
                table[i][j] = False
            if j == 0:
                table[i][j] = True
    
    for i in range(1, length + 1):
        for j in range(1, max_sum + 1):
            if values[i - 1] <= j:
                table[i][j] = table[i - 1][j - values[i - 1]] or table[i - 1][j]
            if values[i - 1] > j:
                table[i][j] = table[i - 1][j]   

    return table[length][max_sum]

values = [3, 34, 4, 12, 5, 2]
length = len(values)
max_sum = 30
dp = [[-1 for i in range(max_sum + 1)] for j in range(len(values) + 1)]
table = [[-1 for i in range(max_sum + 1)] for j in range(len(values) + 1)]
value_recursive = subset_sum_recursive(values, max_sum, length)
value_memoization = subset_sum_memoization(values, max_sum, length)
value_top_down = subset_sum_top_down(values, max_sum, length)

print(value_recursive)
print(value_memoization)
print(value_top_down)

