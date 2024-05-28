#!/usr/bin/env python3
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
class Solution:

    def lengthOfLongestSubstring(self, s:str) -> int:
        # dict to store letter and index
        seen = {}
        # variable to store current start of the index of the substring
        cur_sub_start = 0
        # current substring length
        cur_len = 0
        # variable to store the longest substring
        longest = 0

        for i, letter in enumerate(s):
            if letter in seen and seen[letter] >= cur_sub_start:
                cur_sub_start = seen[letter] + 1
                cur_len = i - seen[letter]
                seen[letter] = i
            else:
                seen[letter] = i
                cur_len += 1
                if cur_len > longest:
                    longest = cur_len
        return longest


sub = Solution()
result = sub.lengthOfLongestSubstring("abcabcbb")
print(result)
