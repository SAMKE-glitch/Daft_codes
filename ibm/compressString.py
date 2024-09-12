#!/usr/bin/env python3
"""
Consider a string, S that is a series of characters, each followed by its frequency
as an integer. The string is not compressed correctly, so there may be multiple
occurrences of the same character. A properly compressed string will consist of one instance
of each character in alphabetical order followed by the total count of that character within the string.
"""
class Solution:
    def stringFreq(self, S: str) -> str:
        #1 iterate the string and pick each character with its subsequent freq and store them to a dictionary
