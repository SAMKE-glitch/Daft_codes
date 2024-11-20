#!/usr/bin/env python3
"""
Given an array nums of n integers,  are there elements a, b, c in nums such that a + b +c = 0?
Find all unique triplets in the array which gives the sum of zero

Notice that the solution set must not contain duplicate triplets

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2], [-1,0,1]]

Example 2:
    Input: nums = []
    Output: []

Example 3:
    Input: nums = [0]
    Output: []

Constraints:
    0 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5
"""
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplets = []
        # n^3 Triple for loop solution
        # here we need to have 3 for loops
        for i in range(len(nums)-2):
            for j in range(len(nums)-1):
                for k in range(len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets.append(tuple(set(nums[i] , nums[j] , nums[k])))
        return(triplets)

sam = Solution()
Input = [-1,0,1,2,-1,-4]
result = sam.threeSum(Input)
print(result)
