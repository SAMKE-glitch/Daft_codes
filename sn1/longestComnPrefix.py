#!/usr/bin/env python3
"""
write a function to find the longest common prefix string amongst an array of
strings.
If there is no common prefix, return an empty string ""


Example 1:
    Input: ["flower", "flow", "flight"]
    Output: "fl"

Example 2:
    Input: ["dog", "racecar", "car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

Note:
    All given inputs are in lowercase letters a-z
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        # Prefix method solution
        pref = strs[0]
        plen = len(pref)

        # iterate through other strings
        for s in strs[1:]:

            # we check or compare if s and the pref
            while pref != s[0:plen]:
                pref = pref[0: (plen - 1)]
                plen -= 1

                if plen == 0:
                    return ""
        return pref

        # we need to check the shortest string in strs that we can use to compare with other strings
        compare_str = min(strs, key=len)

        # we iterate through the index and character in ther compare_str
        for i, char in enumerate(compare_str):

            # iterate through each string in the list strs
            for string in strs:

                # check if the character in characters in string is the same as to that of compare_str
                if string[i] != char:

                    # return the string excluding the i character
                    return compare_str[:i]
        return compare_str


sam = Solution()
Input = ["flower", "flow", "flight"]
result = sam.longestCommonPrefix(Input)
print(result)
