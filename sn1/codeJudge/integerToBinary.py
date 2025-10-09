#!/usr/bin/env python3
"""
function that converts integr to binary

Example: 
    Input: 23
    Output : "10111"
"""

class Solution:
    def integerToBinary(self, number:int) -> str:
        """
        method to convert integer to binary
        Input:
            number(int)
        Return:
            binary(str)
        """
        if not isinstance(number, int):
            raise ValueError("Insert integers only!!!")
        
        # handle negative integers
        if number < 0:
            return "-" + bin(-number)[2:]
        
        # return the converted number and sliced to remove the "ob" from "ob10111"
        return bin(number)[2:]

sam = Solution()
Input = -23
result = sam.integerToBinary(Input)
print(result)
