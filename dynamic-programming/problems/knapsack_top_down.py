# Knapsack using topdown approach
import time
def knapsack_top_down(weights, values, max_weight, length):
    # Initialize the table
    for i in range(length + 1):
        for j in range(max_weight + 1):
            if i == 0 or j == 0:
                table[i][j] = 0

    # Fill the table
    for i in range(1, length + 1):
        for j in range(1, max_weight + 1):
            if weights[i - 1] <= j:
                table[i][j] = max(
                    values[i - 1] + table[i - 1][j - weights[i - 1]],
                    table[i - 1][j])
            else:
                table[i][j] = table[i - 1][j] 

weights = [95, 4, 60, 32, 23, 72, 80, 62, 65, 46]
values = [55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
max_weight = 269
table = [[-1 for i in range(max_weight + 1)] for j in range(len(weights) + 1)]
t_start = time.time()
knapsack_top_down(weights, values, max_weight, len(weights))
print(table[len(weights)][max_weight])
t_total = time.time() - t_start
print('Took {}s'.format(t_total))