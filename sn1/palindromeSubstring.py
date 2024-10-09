#!/usr/bin/env python3
"""
Given a string s, return the longest palindromic substring in s

Example:
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

Example 5:
    1 <= s.length <= 1000
    s consist of only digits and English letters (lower-case and/or upper-case)
"""
class Solution:
    def longestPalindrome(self, s:str) -> str:

        def check_palin(s):
            return(s == s[::-1])

        # check all substrings

        for length in range(len(s), 0, -1):
            for start_index in range(0, len(s)+1-length):
                if check_palin(s[start_index:(start_index+length)]):
                    return s[start_index:(start_index+length)]

sam = Solution()
Input = "babad"
result = sam.longestPalindrome(Input)
print(result)