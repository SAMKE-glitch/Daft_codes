#!/usr/bin.env python3
"""
Given a string, find the length of the longest substring
without repeating characters
Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3

Example 2:
Input: 1
Explanation: The answer is "b", with the length of 1
"""
class lengthOfLongestSubstring(self, s:str) -> int:
    sub = {}
    cur_sub_start = 0
    cur_len = 0
    longest = 0

    for i, letter in enumerate(s):
        if letter in sub and sub[letter] >= cur_sub_start:
            cur_sub_start = sub[letter] + 1
            cur_len = i - sub[letter]
            sub[letter] = i

