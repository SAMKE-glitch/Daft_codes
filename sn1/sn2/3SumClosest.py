#!/usr/bin/env python3
"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution

Example 1:
    Input: nums= [-1,2,1,-4], target = 1
    Output: 2
    Explanation: the sum that is closest to the target is 2 (-1+2+1=2).

Constraints:
    3 <= nums.length <= 10^3
    -10^3 <= nums[i] <= 10^3
    -10^4 <= target <= 10^4
"""
from typing import List



class Solution:
    def threeSumClosest(self, nums:List[int], target: int) -> int:
        best_s = 100000

        nums.sort()

        for i in range(0, len(nums)-2):
            if num[i] == nums[i-1] and i > 0:
                continue

            lower = i + 1
            upper = len(nums) - 1

            while lower < upper:
                s = nums[i] + nums[lower] + nums[upper]
                
                if s == target:
                    return(s)

                if abs(target - s) < abs(target - best_s):
                    best_s = s

                if s <= target:
                    lower += 1
                    while(nums[lower] == nums[lower-1] and lower < upper):
                        lower += 1
                else:
                    upper -= 1
        return(best_s)


