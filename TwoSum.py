#!/usr/bin/env python3
"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may
not use the same element twice.
Example:
    Given numbs = [2, 7, 11], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""
from typing import List

class Solution():
    def add_Two_sum(self, nums: List[int], target: int) -> List[int]:
        #brute force solution or using 2 for loops
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return([i, j])
    
    def Two_sum_dict(self, nums:List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return([seen[target - num], i])
            elif num not in seen:
                seen[num] = i


sam = Solution()
result = sam.add_Two_sum([2, 7, 11], 9)
print(result)
result_2 = sam.Two_sum_dict([2, 7, 11], 9)
print(result_2)
