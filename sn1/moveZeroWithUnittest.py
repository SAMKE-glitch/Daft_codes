#!/usr/bin/env python3
"""
Given an array nums, write a function to move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Example:
    Input: [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

Note:
    1. Do this in-place without making a copy of the array.
    2. Minimize the total number of operations.
"""

from typing import List
import unittest
import timeit

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        no_of_zeroes = nums.count(0)
        not_zeroes_position = 0

        for i in nums:
            if i != 0:
                nums[not_zeroes_position] = i
                not_zeroes_position += 1

        for zero in range(1, no_of_zeroes + 1):
            nums[-zero] = 0

# Unit tests
class TestMoveZeroes(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        nums = [0, 1, 0, 3, 12]
        self.sol.moveZeroes(nums)
        self.assertEqual(nums, [1, 3, 12, 0, 0])

    def test_case_2(self):
        nums = [0, 0, 1]
        self.sol.moveZeroes(nums)
        self.assertEqual(nums, [1, 0, 0])

    def test_case_3(self):
        nums = [1, 2, 3]
        self.sol.moveZeroes(nums)
        self.assertEqual(nums, [1, 2, 3])

    def test_case_4(self):
        nums = [0, 0, 0]
        self.sol.moveZeroes(nums)
        self.assertEqual(nums, [0, 0, 0])

    def test_case_5(self):
        nums = []
        self.sol.moveZeroes(nums)
        self.assertEqual(nums, [])

# Benchmark function
def benchmark():
    setup = '''
from __main__ import Solution
nums = [0, 1, 0, 3, 12] * 1000
s = Solution()
    '''
    stmt = 's.moveZeroes(nums)'
    time = timeit.timeit(stmt=stmt, setup=setup, number=100)
    print(f"\nBenchmark (100 runs): {time:.4f} seconds")

# Entry point
if __name__ == "__main__":
    # Run functional test
    samke = Solution()
    Input = [0, 1, 0, 3, 12]
    samke.moveZeroes(Input)
    print(f"Functional Test Output: {Input}")

    # Run unit tests
    unittest.main(exit=False)

    # Run benchmark
    benchmark()

