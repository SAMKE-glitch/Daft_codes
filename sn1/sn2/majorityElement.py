#!/usr/bin/env python3
"""
Given an array of size n, find the majority element. The majority element is the element that appears
more than n/2 | times.
You may assume that the array is non-ampty and the majority element always exist in the array.

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
        # Solution 1:
        # sorting the array and returning the middle digit

        return sorted(nums)[len(nums) // 2]
        # SOLUTION 2:
        # create an empty dictionary
        sums = {}

        # loop through the nums
        for n in nums:
            if n not in sums:
                sums[n] = 1
            else:
                sums[n] +=1

            # check if n is greater than nums/2
            if sums[n] > len(nums)/2:
                return n

sam = Solution()
Input = [2,2,1,1,1,2,2]
result = sam.majorityElement(Input)
print(result)
