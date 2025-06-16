#!/usr/bin/env python3
"""
Given an array nums, write a function to move all 0's to the end of it while maintaiining the relative
order of non-zero elements.

Example:
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]

Note:
    1. You must do this in-place without making a copy of the array.
    2. Minimize the total number of operations
"""
import typing

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anythin,
        modify nums in-place instead.
        """
        zero_count = nums.count(0)

        next_non_zero = 0

        for num in nums:
            if num != 0:
                nums[next_non_zero] = num
                next_non_zero += 1

            for zero in range(1, zero_count + 1):
                nums[-zero] = 0

samke = Solution()
Input = [0,1,0,3,12]
result = samke.moveZeroes(Input)
print(result)

