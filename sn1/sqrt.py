#!/usr/bin/env python3
"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is returnedi.

Example 1:
    Input: x = 4
    Output: 2

Example 2:
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842...., and since the decimal part
                is truncated, 2 is returned

Constraints:
    0 <= x <= 2^31 - 1
"""
import math
import cmath

class Solution:
    def sqrt(self, x:int) -> int:
        # A way to  handle both negative and positive numbers

        if x < 0:
            return cmath.sqrt(x)
        else:
            return math.sqrt(x)
        # using exponentiation solution
        return int(int( x**(1/2)))



        # using the sqrt function
        return int(sqrt(x))


sam = Solution()
Input = 4
result = sam.sqrt(4)
print(result)
