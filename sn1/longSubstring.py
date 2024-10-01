#!/usr/bin/env python3
"""
Given a string, find the length of the longest substring without repeating
characters

Example 1:
    Input: "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3

Example 2:
    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1

Example 3:
    Input:  "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
                NOTE-> That the answer must be a substring, "pwke" is 
                a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # we need to keep a dictionary that sores the letters we've seen
        sub = {}
        # we need to keep track of the index of our current substring is starting from
        cur_sub_startIndex = 0
        # current length of our substring we've seen so far
        cur_len = 0
        # longest substring so far
        longest = 0
        # example of a string "abcdecfab"

        # loop through every letter in string s and also need index position, so use enumerate
        for i, letter in enumerate(s):
            if letter in sub and sub[letter] >= cur_sub_startIndex:


