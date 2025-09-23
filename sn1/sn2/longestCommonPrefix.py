#!/usr/bin/env python3
"""
Write a function to find the longest common prefix string amongst an arrayof strings.
If there is no common prefix, return an empty string ""

Example 1:
    Input: ["flower", "flow", "flight"]
    Output: "fl"

Example 2:
    Input: ["dog", "racecar", "car"]
    Output: ""
    Explanation: there is no common prefix among the input strings

Note: All given inputs are in lowercase letters a-z
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs:List[str]) -> str:
        # handling when the strs is empty
        if len(strs) == 0:
            return("")

        # handling when length is one
        if len(strs) == 1:
            return(strs[0])
