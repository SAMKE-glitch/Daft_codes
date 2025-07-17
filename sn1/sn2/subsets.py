#!/usr/bin/env python3
"""
Givenan integer array nums of unique elements, return all possible subsets (the powerset).
The solution set must not contain duplicate subsets. Return the solution in order.

Example 1:
    Input: nums = [1, 2, 3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:
    Input: nums = [0]
    Output: [[], [0]]

Constraints:
    1 <= num.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Method 1: Longer solution, naive solution

        # Start with the empty subset
        result = [[]]

        for num in nums:
            # For each exisiting subset, create a new subset that includes the current number
            new_subsets = []
            for subset in result:
                new_subsets.append(subset + [num])

            # Add all the new subsets to our result
            result += new_subsets
        return result

samke = Solution()
Input = [1, 2, 3]
Output = samke.subsets(Input)
print(Output)
