#!/usr/bin/env python3
"""
Welcome to your very first hands-on experience with Binary Search! Excited? You certainly should be!

Imagine that you're working on an e-commerce platform, and there's a customer looking for a product at a specific price. This customer needs to know if such a product exists on the platform.

To assist this customer, we will implement Binary Search on a sorted list of product prices.
"""
from typing import List


class Solution:
    def binary_search_iterative(self, data:List[int], target:int) -> int:
        low = o
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
