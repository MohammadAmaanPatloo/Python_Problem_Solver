"""
Problem Statement

You are given a list where each element represents the price of a stock on a particular day.

You can:

Buy once
Sell once
You must buy before you sell

Return the maximum profit you can make.

If no profit is possible, return 0.

Example 1
prices = [7, 1, 5, 3, 6, 4]

Output:
5
"""


def max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        # Update the minimum price
        if price < min_price:
            min_price = price

        # Calculate current profit
        profit = price - min_price

        # Update maximum profit
        if profit > max_profit:
            max_profit = profit

    return max_profit


# Example usage
print(max_profit([7, 1, 5, 3, 6, 4]))  # 5
print(max_profit([7, 6, 4, 3, 1]))  # 0
print(max_profit([2, 4, 1]))  # 2
