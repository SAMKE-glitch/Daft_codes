#!/usr/bin/env python3
"""
Demostration and understanding of Hash Functions and Hashing
"""


class Solution:
    def simpleHash(self, inputString: str) -> int:
        summation = sum(ord(ch) for ch in inputString)

        # We limit our hash range from 0 to 9
        return summation % 10


samke = Solution()
print(samke.simpleHash("Hello"))
