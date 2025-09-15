#!/usr/bin/env python3
"""
Given an array nums of n integers, are there elements a, b,c in nums such that
a + b + c = 0? Find all the unique triplets in the array which gives the sum of zero.
Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: num = [-1,0,1,2,-1,4]
    Output: [[-1,-1,2], [-1,0,1]]

Example 2:
    Input: nums = []
    Output: []

Example 3:
    Input: nums = [0]
    Output = []

Constraints:
    0 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
