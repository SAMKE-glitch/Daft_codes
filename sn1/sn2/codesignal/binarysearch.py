#!/usr/bin/env python3
"""
Welcome to your very first hands-on experience with Binary Search! Excited? You certainly should be!

Imagine that you're working on an e-commerce platform, and there's a customer looking for a product at a specific price. This customer needs to know if such a product exists on the platform.

To assist this customer, we will implement Binary Search on a sorted list of product prices.
"""
from typing import List


class Solution:
    products_price = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
    def binary_search_iterative(self, data:List[int], target:int) -> int:
        low = 0
        high = len(data)

        while high - low > 1:
            mid = (high + low) // 2

            if target < data[mid]:
                high = mid
            elif target > data[mid]:
                low = mid
            else:
                # if target is equal to data[mid]
                return mid
        return low if data[low] == target else None

    def search_price(self, customer_query: int) -> int:
        result = self.binary_search_iterative(products_price, customer_query)

        if result is not None:
            print(f"Product of price ${customer_query} is found at position {result} in the price list.")
        else:
            print(f"No product is found with the price ${customer_query}.")


samke = Solution()
samke.search_price(30)
samke.search_price(31)
