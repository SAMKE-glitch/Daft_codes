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
        # parameters to store value previous height[start] and height[ends]
        prev_start = 0
        prev_end = 0

        while start != end:
            if height[start] < prev_start:
                start += 1
                continue
            if height[end] < prev_end:
                end -= 1
                continue

            next_area = min(height[start], height[end]) * (end - start)
            if next_area > largest:
                largest = next_area

            if height[start] < height[end]:
                prev_start = height[start]
                start += 1
            else:
                prev_end = height[end]
                end -= 1
        return largest

sam = Solution()
Input = [1,8,6,2,5,4,8,3,7]
result = sam.maxArea(Input)
print(result)

