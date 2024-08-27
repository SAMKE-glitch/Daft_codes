#!/usr/bin/env python3
"""
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

Note:
    1. You must do this in-place without making a copy of the array.
    2. Minimize the total number of operations.
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead
        """
        zero_count = nums.count(0)
        next_non_zero = 0

        for n in nums:
            if n != 0:
                nums[next_non_zero] = n
                next_non_zero += 1

