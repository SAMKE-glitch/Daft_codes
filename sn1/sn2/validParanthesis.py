#!/usr/bin/env python3
"""
Given a string s containing just the characters '(', ')', '{', '}, '[' and ']',
dtermine if the input string is valid.
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
    Output = false

Example 5:
    Input: s = "{[]}"
    Output: true

Constraints:
    1 <= s.length <= 10^4
    s consists of paranetheses only '()[]{}'
"""
class Solution:
    def isValid(self, s: str) -> bool:

