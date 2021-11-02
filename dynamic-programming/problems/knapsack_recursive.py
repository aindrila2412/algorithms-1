# Knapsack problem using recursion
def knapsack(weights, values, max_weight, length):
    # Base condition 
    if len(weights) == 0 or length == 0:
        return 0 

    if weights[-1] <= max_weight:
        return max(
            values[-1] + knapsack(weights[:-1], values[:-1], max_weight - weights[-1], length - 1),
            knapsack(weights[:-1], values[:-1], max_weight, length - 1)
            )
    if weights[-1] > max_weight:
        return knapsack(weights[:-1], values[:-1], max_weight, length - 1)

weights = [95, 4, 60, 32, 23, 72, 80, 62, 65, 46]
values = [55, 10, 47, 5, 4, 50, 8, 61, 85, 87]
max_weight = 269
length = 10
print(knapsack(weights, values, max_weight, length))