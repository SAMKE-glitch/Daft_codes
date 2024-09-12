#!/usr/bin/env python3
"""
culcResult method
"""
from typing import List


class Solution:
    def culcResult(self, Input: List[str]) -> int:
        # getting the cards dealt
        cards = [int(x) if x.isdigit() else x for x in Input]
        if '0' in Input:
            #remove highest card if '0' is present
            cards.remove(max(cards))
        # sum all integer cards
        total = sum([x for x in cards if isinstance(x, int)])
        if '10x' in cards:
            total += max([x for x in cards if isinstance(x, int)]) * 9
        return total





sam = Solution()
Input = ['0', '4', '5', '9', '10x']
result = sam.culcResult(Input)
print(result)
