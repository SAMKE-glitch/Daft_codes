#!/usr/bin/env python3
"""
Given two strings, str1, and str2, where str1 contains exactly one character more than str2, find the indices of the characters in str1 that can be removed to make str1 equal to str2. Return the array of indices in increasing order. If it is not possible, return the array \[-1\]. 

**Note:** Use 0-based indexing.

**Example**

str1 = "abdgggda"

str2 = "abdggda"

Any "g" character at positions 3, 4, or 5 can be deleted to obtain str2.
"""
from typing import List


class Solution:
    def getRemovableIndices(self, str1: str, str2: str) -> List[int]:
        # Step 1: Ensure str1 is exactly one character longer
        # Edge case: Str must be longer than str2 by 1 char
        if len(str1) != len(str2) + 1:
            return[-1]
        
        # Step 2: Store valid indices where a char can be removed
        removableIndeces = []

        # Step 3: Try removing each character one-by-one
        for i in range(len(str1)):
            newStr = str1[:i] + str1[i+1:]
            
            if newStr == str2:
                removableIndeces.append(i)

        # Step 4: Return result list, or [-1] if empty

        if len(removableIndeces) > 0:
            return(removableIndeces)
        else:
            return([-1])
