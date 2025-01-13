#!/usr/bin/env python3
"""
Given a string containing digits from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given
below. Note that 1 does not map to any letters.

Example 1:
    Input: digits = "23"
    Output: ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']

Example 2:
    Input: digits = "2"
    Output: ['a', 'b', 'c']

Example 3:
    Input: digits = ""
    Output: []

Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9']
"""
from typing import List


class Solution:
    def letterCombinations(self, digits:str) -> List[str]:
        phone_map = {'2': 'abc', '3': 'def', '4': 'fgh', '5': 'ijk',
                       '6': 'mno', '7': 'pqrx', '8': 'tuv', '9': 'wxyz'}

        # so we need a double for loop to achieve this
        # example "23"
        # we need to extract the value of the key in phone_map and make it a list

        # handle the edge case when the list is an empty string
        if digits == "":
            return([])
        # extracting the number from the dictionary mapped to the digits
        numbers = list(phone_map[digits[0]])

        for digit in digits[1:]:
            numbers = [old+new for old in numbers for new in list(phone_map[digit])]
        return numbers



sam = Solution()
digits = "79"
result = sam.letterCombinations(digits)
print(result)

