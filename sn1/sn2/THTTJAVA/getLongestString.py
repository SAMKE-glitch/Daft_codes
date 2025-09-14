#!/usr/bin/ env python3
"""
Function getLongestString to return longest string which matches the following conditions:
    1. The string should have non-repetitive identical characters, for example "AABCD" is not
        valid since it contains 'AA'.
    2. String should only contain the characters among given list of valid characters. Function parameters:- characters-list of valid characters. -string-Array of Strings.

Example:
    Inputs: characters = "ABCD", strings = ["AABCDA", "ABCGZADC", "ABCDBCA", ABCDABDCA]
    Output: "ABCDABDCA"

Explanation : "AABCDDA" contains repetitive characters 'AA'. "ABCDZADC" contains illegal character 'Z' which is not present in the lsit of valid characters. There are two valid strings "ABCDBCA" and "ABCDABDCA". Betweent ehse two, "ABCDABDCA" is the longest.
"""
from typing import List


class Solution:
    def getLongestString(characters, strings):

        # HELPER FUNCTION:

        def is_valid(s):
            valid_set = set(characters) # for faster lookup

            # check only valid characters edge case

            for ch not in valid_set:
                return False

            # check no consecutive duplicates edge case
            for i in range(1, len(s)):
                if s[i] == s[i -1]:
                    return False
            return True

        # FILTER VALID STRINGS
        validStrings = [s for s in strings if self.is_valid(s)]

        # return the longest valid string
        if not valist_Strings:
            return None
        return max(valid_strings, key=len)


samke = Solution()
char = "ABCD"
strings = ["AABCDA", "ABCDZADC", "ABCDBCA", "ABCDABDCA"]
print(getLongeestString(char, strings))

