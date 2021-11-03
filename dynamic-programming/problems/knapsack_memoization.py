import time
# Knapsack problem using memoization
def knapsack(weights, values, max_weight, length):
    # Base condition 
    if len(weights) == 0 or length == 0:
        return 0 
    
    if dp[length][max_weight]!= -1:
        return dp[length][max_weight]


    if weights[-1] <= max_weight:
        dp[length][max_weight] = max(
            values[-1] + knapsack(weights[:-1], values[:-1], max_weight - weights[-1], length - 1),
            knapsack(weights[:-1], values[:-1], max_weight, length - 1)
            )
        return dp[length][max_weight]
    if weights[-1] > max_weight:
        dp[length][max_weight] = knapsack(weights[:-1], values[:-1], max_weight, length - 1)
        return dp[length][max_weight]


weights = [95, 4, 60, 32, 23, 72, 80, 62, 65, 46]
values = [55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
max_weight = 269
length = 10
dp = [[-1 for i in range(max_weight + 1)] for j in range(length + 1)]
t_start = time.time()
print(knapsack(weights, values, max_weight, length))
t_total = time.time() - t_start
print('Took {}s'.format(t_total))