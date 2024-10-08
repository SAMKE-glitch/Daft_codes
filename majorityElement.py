#!/usr/bin/env python3
"""
Given an array of size n, find the majority element. The majority element is the element
that appears more than n/2 | times.
You may assume that the array is non-empty and the majority element alwaysexist in the array.

Example 1:
    Input: [3,2,3]
    Output: 3

Example 2:
    Input: [2,2,1,1,1,2,2]
    Output: 2
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """# dictionary way to solve
        sums = {}

        for n in nums:
            if n not in sums:
                sums[n] = 1
            else:
                sums[n] += 1
            if sums[n] > len(nums) / 2:
                return n"""
        # sorted way
        return sorted(nums)[len(nums)//2]

sam = Solution()
Input = [2,2,1,1,1,2,2]
result = sam.majorityElement(Input)
print(result)
