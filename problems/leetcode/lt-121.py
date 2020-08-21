# 121. Best Time to Buy and Sell Stock

"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Input: [7,1,5,3,6,4]
Output: 5
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum_price = float('inf')
        maximum_profit = 0
        difference = 0

        for i in prices:
            minimum_price = min(minimum_price, i)
            difference = i - minimum_price 
            maximum_profit = max(maximum_profit, difference)
        return maximum_profit
        