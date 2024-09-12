#!/usr/bin/env python3
"""
culcResult method
"""
from typing import List


class Solution:
    def culcResult(self, Input: List[str]) -> int:
        # List convert from str to int
        # ['0', '4', '5', '9', '10x']
        sumInt = 0

        # iterate the list
        for i in Input:
            if i == '10x':
                sumInt *= 10
            else:
                sumInt += int(i)
        return sumInt


sam = Solution()
Iput = ['0', '4', '5', '9', '10x']
result = sam.culcResult(Iput)
print(result)
