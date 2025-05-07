#!/usr/bin/env python3
"""
Given an array nums, write a function to move al 0's to the end of it
while maintaining the relative order of the non-zero elements.

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
        no_of_zeroes = c=nums.count(0)
        not_zeroes_position = 0

        for i in nums:
            if i != 0:
                nums[i-1] = i
                not_zeroes_position +=1

        for zero in range(1, len(no_of_zeroes)+1):
            nums[-zero] = 0


samke = Solution()
Input = [0,1,0,3,12]
