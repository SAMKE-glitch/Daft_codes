#!/usr/bin/env python3
"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb
to the top?

Example 1:
    Input: 2
    Output: 2

    Explanation: There are two ways to climb to the top.

    1. 1 step + 1 step
    2. 2 steps

Example 2:
    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 step
    3. 2 step + 1 step

Constraints:
    1 <= n <= 45
"""
from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        a, b = 1, 2

        for i in range(3, n+1):
            a, b = b, a+b
        return b


samke = Solution()
Input = 5
result = samke.climbStairs(Input)
print(result)
