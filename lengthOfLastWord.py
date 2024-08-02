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
"""
import typing


class Solution:
    def lenOfLastWord(self, s:[str]) -> int:
        if len(s) == 0:
            return 0
        lastWord = s - 1
        return len(lastWord)

sam = Solution()
Input = "Hello World"
result = sam.lenOfLastWord(Input)
print(result)
