#!/usr/bin/env python3
"""
Given a string s, return the longest palindromic substring in s
Example 1:
    Input: s = "babad"
    Output: "bab"
    Note: "aba" is also a valid answer

Example 2:
    Input: s = "cbbd"
    Output: "bb"

Example 3:
    Input: s = "a"
    Output: "a"
Example 4:
    Input: s = "ac"
    Output: "a"

Constraints:
    -> 1 <= s.lenght <= 1000
    -> s Consist of only digits and English letter (lower-case and/or upper-case)
"""
class Solution():
    def longestPalindrome(self, s: str) -> str:

        def check_palin(s: str) -> bool:
            return(s == s[::-1])

        
