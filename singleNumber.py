#!/usr/bin/env python3
"""
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

NOTE: You algorithm should have a linear runtime complexity. Could you implement
it without using extra memory?

Example 1:
    Input: [2,2,1]
    Output: 1

Example 2:
    Input: [4,1,2,1,2]
    Output: 4
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # the dictionary method to store counts
        counts = {}
        
        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                del counts[n]
        return list(counts.keys())[0]
        # Bitwise XOR Bit manipulation https://www.geeksforgeeks.org/python-bitwise-operators/

sam = Solution()
Input = [4,1,2,1,2]
result = sam.singleNumber(Input)
print(result)
