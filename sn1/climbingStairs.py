#!/usr/bin/env python3
"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinc ways can you climb
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
    Explanation: There a re three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

Constraints:
    1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # dictionary to store key and value
        path = {1:1, 2:2, 3:3}
        for x in range(4, n+1):
            path[x] = path[x-1] = path[x-2]
        return(path[n])

sam = Solution()
Input = 4
result = sam.climbStairs(Input)
print(result)
