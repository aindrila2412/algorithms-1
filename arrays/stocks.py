"""
	Given an array of numbers consisting of daily stock prices, 
	calculate the maximum amount of profit that can be made from buying on one day and selling on another.

	Return the maximum profit.
"""
def buy_and_sell_stock_once(prices):
	minimum_price = float('inf')
	maximum_profit = 0
	difference = 0

	for i in prices:
		minimum_price = min(minimum_price, i)
		difference = i - minimum_price 
		maximum_profit = max(maximum_profit, difference)
	return maximum_profit


print(buy_and_sell_stock_once([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))

