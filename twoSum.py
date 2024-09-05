#!/usr/bin/env python3
"""
Given an array of integers, return indices of the two numbers such that 
they add to a specific target.
You may assume that each input would have exactly one solution, and you may 
not use the same element twice

Example:
    Given nums = [2, 7, 11, 15], target = 9
    Because nums[0] + nums[1] = 2 +7 = 9,
    return [0, 1]
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # the for loop solution Bruteforce
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] = target:
                    return([i, j])
