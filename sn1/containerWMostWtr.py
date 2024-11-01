#!/usr/bin/env python3
"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, a).
n vertical lines are drawn such that the two endpoints of line i is at (i,ai) and (i, 0). Find
two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example: Input: [1,8,6,2,5,4,8,3,7]
        Output: 49
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # variable to hold the first index
        start = 0
        # variable to hold the last index
        end = len(height) - 1
        largest = 0

