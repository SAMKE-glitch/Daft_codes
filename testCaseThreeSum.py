#!/usr/bin/env python3
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        # handle the edge cases
        if len(nums) < 3:
            return []

        nums.sort()  # Sorting the array

        # Two-pointer approach
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break  # If nums[i] is positive, sum can't be zero
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicate values of nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1  # Skip duplicate values of nums[left]
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1  # Skip duplicate values of nums[right]
                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return triplets

# Test case
sam = Solution()
Input = [-1, 0, 1, 2, -1, -4]
result = sam.threeSum(Input)
print(result)

