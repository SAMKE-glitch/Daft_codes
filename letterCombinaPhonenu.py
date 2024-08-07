#!/usr/bin/env python3
"""
Given a string containing digit from 2-9 inclusive, return all possible letter
combinations that the number could represent. Return the answer in any order.
A mappinf of digit to letters(just like on the telephone buttons) is given below.
Note that 1 does not map to any letters
Example 1:
    Input: digit = "23"
    output: ["ad", "ae", "af", "bd", "be", "cd", "ce", "cf"]

Example 2:
    Input: digits = ""
    Output: []

Example 3:
    Input: digits = "2"
    Output: ["a", "b", "c"]

Constraints:
    0 <= digits.length <= 4
    digits[i] is a digit in the range ['2', '9']
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #creating the dictionary for mapping
        phone_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno",
                     "7": "pqrs", "8": "tuv", "9": "wxyz"}

        #edge case
        if digits == "":
            return []
        # creating numbers variable to store the letters or characters list in that digit
        # e.g 2 for [a, b, c]
        numbers = list(phone_map[digits[0]])
        for digit in digits[1:]:
            numbers = [old+new for old in numbers for new in list(phone_map[digit])]
        return numbers

sam = Solution()
Input = "23"
result = sam.letterCombinations(Input)
print(result)
