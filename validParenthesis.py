#!/usr/bin/env python3
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

    Example 1:
    Input: s = "()"
    Output: true

    Example 2:
    Input: s = "()[]{}"
    Output: true

    Example 3:
    Input: s = "(]"
    Output: false

    Example 4:
    Input: s = "([)]"
    Output: false

    Example 5:
    Input: s = "{[]}"
    Output: true

    Constraints:
    1 <= s.length <= 10^4
    s consists of parenthesis only "()[]{}"
"""
class Solution:
    def isValid(self, s: str) -> bool:

        # Optimized solution && Efficient one
        # Close the last seen opening symbol w/ stack
        close_map = {"{":"}", "[":"]", "(":")"}
        opens = []
        for symbol in s:
            if symbol in close_map.keys():
                opens.append(symbol)
            elif opens == [] or symbol != close_map[opens.pop()]:
                return False
        return opens == []

        # Inner string replace method
        """
        replace = True
        while replace:
            start_length = len(s)
            for inner in ["{}", "[]", "()"]:
                s = s.replace(inner, "")
            if start_length == len(s):
                replace = False
        return s == """""

sam = Solution()
Input = "([)]"
result = sam.isValid(Input)
print(result)
