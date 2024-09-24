#!/usr/bin/env python3
"""
Your task is to write the function maxProfit that calculates the maximum
profit achievable from these transactions (profit = selling price - buying price).
If a profit isn't attainable, the function should return the lowest stock price
of the day. The function takes two parameters as inputs - The prices array that contains the share price over the day (prices), and the number of entries in the prices array (n).
It then calculates and returns the maximum profit that could have been achieved that day.

Example 1:
    Input: n=5
           prices = [10,12,9,11,12]
    Output: 3
    Explanation: The lowest price is 9 and the highest price is 12
                so 12 - 9 = 3
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], n: int) -> int:
        if n == 0:
            return 0
        # we need to declare 2 parameters one for maxProf and minimum price
        min_price = prices[0]
        maxProfit = 0

        for i in range(1, n):
            current_profit = prices[i] - min_price

            if prices[i] < min_price:
                min_price = prices[i]

            if current_proft > maxProfit:
                maxProfit = current_profit
        return maxProfit

