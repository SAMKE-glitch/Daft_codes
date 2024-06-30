#!/usr/bin/env python3
"""
given n non-negative integers a1, a2, ... An, where each represents
a point at cordinate (i, ai). n vertical lines are drawn such that two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container
such that the container contains the most water.
Note:
    You may nt slant the container and n is at least 2
Example:
    Input: [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output : 49
"""
from typing import List


class Solution():
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        largest = 0
        prev_start = 0
        prev_end = 0

        while start != end:
            if height[start] < prev_start:
                start += 1
                continue
            if height[end] < prev_end:
                end -= 1
                continue
            new_area = min(height[start], height[end]) * (end - start)

            if new_area > largest:
                largest = new_area

            if start < end:
                start += 1
            if end < start:
                end -= 1
        return largest

s = [1, 8, 6, 2, 5, 4, 8, 3, 7]
test = Solution()
result = test.maxArea(s)
print(result)
