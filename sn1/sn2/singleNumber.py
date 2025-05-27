#!/usr/bin/env python3
"""
Given a non-empty array of integers, every element appears twice except for one.
Find that single one.

Note:
    Your algorithm should have a linear runtime complexity. Could you implement it
    without using extra memory?

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
        sums = {}

        for num in nums:
            if num not in sums:
                sums[num] = 1
            else:
                del(sums[num])
        return list(sums.keys())[0]

samke = Solution()
Input = [2, 2, 1]
result = samke.singleNumber(Input)
print(result)
