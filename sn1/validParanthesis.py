#!/usr/bin/env python3
"""
Given a string s containing just characters '(', ')', '{', '}', '[' and 
']', determine if the input string is valid.
An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order

Example 1:
    Input: s = "()"
    Output: true

Example 2:
    Input: s = "()[]{}"
    Output: true

Example 3:
    Input: s= "(]"
    Output: false

Example 4:
    Input: s = "([)]"
    Output: false

Example 5:
    Input: s = "{[]}"
    Output: true

Constraints:
    1 <= s.length <= 10^4
    s consists of parentheses only "()[]{}"
"""


class Solution:
    def isValid(self, s: str) -> bool:

        # inner string replace method

        # have a loop to keep on track if we can replace something in our string
        # we are going to have a variable track if we're able to replace something
        replace = True
        while replace:
            start_length = len(s)
            for inner in ["()", "{}", "[]"]:
                s = replace(inner, "")
            if start_length = len(s):
                replace = False
        return s == ""
