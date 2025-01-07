#!/usr/bin/env python3
"""
Given an array nums of n integers and an integer target, find three integers in nums
such that the sum is closest to target. Return the sum of the three integers. You may assume
that each input would have exactly one solution

Example 1:
    Input: nums = {-1, 2, 1, -4}, target = 1
    Output: 2
    Explanation: The sum that is closest to the target is 2. {-1 + 2 + 1 = 2}

Constraints:
    3 <= nums.length <= 10^3
    -10^3 <= nums[i] <= 10^3
    -10^4 <= target <= 10^4.
"""
from typing import List


class Solution:
    def ThreeSumClosest(self, nums:List[int], target:int) -> int:
        # so we need to sort the array in order to avoid a for loop on n^3
        nums.sort()

        best_sum = 10000

        for i in range(0, len(nums)-2):
            if nums[i] == nums[i-1] and i > 0:
                continue

            lower = i+1
            upper = len(nums)-1

            while lower < upper:
                s = nums[i] + nums[lower] + nums[upper]
                if s == target:
                    return s
