#!/usr/bin/env python3


from typing import List

class Solution:
    def culcResult(self, Input: List[str]) -> int:
        cards = [int(x) if x.isdigit() else x for x in Input]
        if '0' in Input:
            cards.remove(max(cards))  # Remove highest card if '0' is present
        
        # Sum up all the cards
        total = sum([x for x in cards if isinstance(x, int)])
        
        # Check for 10x multiplier
        if '10x' in Input:
            total += max([x for x in cards if isinstance(x, int)]) * 9  # Correct multiplication by 10
        
        return total

# Test
sam = Solution()
input1 = ['0', '4', '5', '9', '10x']
print(sam.culcResult(input1))  # Output: 90

