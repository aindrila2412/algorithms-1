# Given an array arr[] of length N and an integer X, the task is to find the number of subsets with a sum equal to X.
"""
    Input: arr[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Target = 11
    Output: 4
"""

# Approach 1: Using recursion (backtracking)
def recursive_subset_count(arr, n, max_sum):
    if max_sum == 0:
        return 1
    if n == 0:
        return 0
    if arr[n-1] > max_sum:
        return recursive_subset_count(arr, n-1, max_sum)
    return recursive_subset_count(arr, n-1, max_sum) + recursive_subset_count(arr, n-1, max_sum-arr[n-1])


# Approach 2: Using Dynamic Programming
def dp_subset_count(arr, n, max_sum):
    dp = [[0 for i in range(max_sum+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(1, n+1):
        for j in range(1, max_sum+1):
            if arr[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-arr[i-1]]
    return dp[n][max_sum]

# Approach 3: Using recursion to count all the subsets
def recursive_subset_check_count(ip, op, final, target):
    if ip == []:
        if sum(op) == target:
            final.append(op)
        return
    recursive_subset_check_count(ip[1:], op, final, target)
    recursive_subset_check_count(ip[1:], op + [ip[0]], final, target)


final = []
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 11
recursive_subset_check_count(arr, [], final, target)
print(final)
print(len(final))

print(dp_subset_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 11))
print(recursive_subset_count([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 11))