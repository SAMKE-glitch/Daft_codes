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
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
