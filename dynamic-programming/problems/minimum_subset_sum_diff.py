# Minimum subset sum difference 
"""
    Given an array of integers, find the minimum sum which is obtained from subtracing each two integers product.

    Input: [1, 6, 11, 5]
    Output: 1 
"""
def minimum_subset_sum_diff(values, max_sum):
    dp = [[-1 for _ in range(max_sum + 1)] for _ in range(length + 1)]
    for i in range(len(values) + 1):
        for j in range(max_sum + 1):
            if i == 0:
                dp[i][j] = 0
            if j == 0:
                dp[i][j] = 1
    # Return the last row of the dp table
    for i in range(1, len(values) + 1):
        for j in range(1, max_sum + 1):
            if values[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - values[i - 1]] or dp[i - 1][j]
            if values[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
    return dp[len(values)]

values = [1, 6, 11, 5]
max_sum = sum(values)
length = len(values)
vals = minimum_subset_sum_diff(values, max_sum)
minimum = float('inf')
for i in range(len(vals) // 2):
    if vals[i] == 1:
        minimum = min(minimum, max_sum - 2 * (i))
print(minimum)
