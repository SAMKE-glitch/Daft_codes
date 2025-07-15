#!/usr/bin/env python3
"""
Given a string s consists of some words separated by spaces, return the length
of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-spcae characters only

Example 1:
    Input : s = "Hello World"
    Output: 5

Example 2:
    Input: s = " "
    Output: 0

Constraints:
    1 <= s.length <= 10^4
    s consists of only English letters and spaces ' '
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Method 1: String split version
        if s.split():
            return len(s.split()[-1])
        return 0

samke = Solution()
Input = "Hello World"
result = samke.lengthOfLastWord(Input)
print(result)
