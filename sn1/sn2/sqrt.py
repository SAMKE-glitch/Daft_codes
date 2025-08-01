#!/usr/bin/env python3
"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is return

Example 1:
    Input: x = 4
    Output: 2

Example 2:
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842...., and since the decimal part is truncated, 2 is returned

Constraints:
    0 <= x <= 2^31 -1
"""


from math import sqrt


class Solution:
    def mySqrt(self, x: int) -> int:

        # exponent solution
        return int(x**(1/2))


        # import solution
        return sqrt(x)
samke = Solution()
Input = 8
result = samke.mySqrt(Input)
print(result)
