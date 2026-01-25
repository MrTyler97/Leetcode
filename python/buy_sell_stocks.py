"""
Docstring for python.buy_sell_stocks

You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

Example 1:

Input: prices = [10,1,5,6,7,1]

Output: 6

Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.
"""
#My solution
def maxProfit(prices: list[int]) -> int:
    profit = 0
    #Start at fist index (bought)
    for cur in range(len(prices)):
        #Start at index after cur (sell)
        for future in range(cur + 1, len(prices)):
            #subract sell from bought and replace profit if greater
            if (prices[future] - prices[cur]) > profit:
                profit = prices[future] - prices[cur]
    return profit

prices = [10,8,7,5,2]
print (maxProfit(prices))