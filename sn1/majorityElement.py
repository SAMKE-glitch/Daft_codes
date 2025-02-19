#!/usr/bin/env python3
"""
Given an array of size n, find the majority element. The majority element is the element that
appears more than n/2 | times.
You may assume that the array is non-empty and the majority element always exist in the array.

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
        # solution 2 1 one line solutio asuuming the ,majority sits at the midle when sorted
        return sorted(nums)[len(nums)//2]
        # creates a dictionary that is going to loop through nums
        sums = {}
        for n in nums:
            if n not in sums:
                sums[n] = 1
            else:
                sums[n] += 1
            if sums[n] > len(nums)/2:
                return(n)

sam = Solution()
Input = [3,2,3]
result = sam.majorityElement(Input)
print(result)
