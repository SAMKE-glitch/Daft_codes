#!/usr/bin/env python3
"""
Given a string S consits of some words separated by spaces, return the length of the last word in the string.
If the last word does not exist, return 0.
Aword is a maximal substring consisting of non-space characters only.

Examples 1:
    Input: s = "Hello World"
    Output: 5

Example 2:
    Input: s = ""
    Output: 0

Constraints:
    1 <= s.length <= 10^4
    s consists of only English letters and spaces ' '
"""
import typing


class Solution:
    def lenOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        if not words:
            return 0
        return len(words[-1])

sam = Solution()
Input = " "
result = sam.lenOfLastWord(Input)
print(result)
