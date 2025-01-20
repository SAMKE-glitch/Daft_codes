#!/usr/bin/env python3
"""
Given a string s consists of some words separated by spaces,
return the length of the last word in the string if the last word
does not exist, return 0.

A WORD is a maximal substring consisting of non-space characters only.

Example 1:
    Input: s = "Hello World"
    Output: 5

Example 2:
    Input: s = " "
    Output: 5

Constraints:
    1 <= s.length <= 10^4
    s consists of only English letters and spaces ' '.
"""


class Solution:
    def lengthOfLastWord(self, s:str) -> int:

        # method 2: a fast one for manual counting the string's last word
        count = 0

        for letter in s[::-1]:
            if letter == " ":
                if count >=1:
                    return count
            else:
                count += 1
        return count
        # method 1: using python string manipulation method split method
        if s.split():
            return len(s.split()[-1])
        return 0


sam = Solution()
Input = "Hello World"
result = sam.lengthOfLastWord(Input)
print(result)
