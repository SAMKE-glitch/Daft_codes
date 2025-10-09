#!/usr/bin/env python3
"""
Excellent work, astronaut! As the final step in our exploration of Binary Search, you have a mission to undertake!

Consider this exciting real-life scenario: you possess a sorted list of grades for a class, and a student is eager to ascertain his/her position within the list. Your assignment is to implement Binary Search on this list to locate the specific position of a given grade.

Prepare yourself for an exciting journey!
"""
from typing import List


class Solution:
    grades = [35, 42, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

    def binary_search(self, grades:List[int], target:int) -> int:
        low = 0
        high = len(grades)

        while high - low > 1:
            mid = (high + low) // 2

            if target < grades[mid]:
                high = mid
            else:
                low = mid
        return low if grades[low] == target else None


samke = Solution()
Input = 75
result = samke.binary_search(samke.grades, Input)
print(result)

