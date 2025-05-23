#!/usr/bin/env python3
"""
Function to add 2 binary numbers

Example:
    Input: "1010", "1101"
    Output: "10111"
"""
class Solution:
    def addBinary(self, a:str, b:str) -> str:

        if not (a.isdigit() and b.isdigit() and set(a) <= {"0", "1"} and set(b) <= {"0", "1"}):
            raise ValueError("insert binaries only!!")
        # convert the binary to integer for easy adding
        # using base 2, because binaries are in base 2
        bin1 = int(a, 2)
        bin2 = int(b, 2)

        total = bin1 + bin2
        print(total)

        # convert back to binarries
        return bin(total)[2:] # Here we have the slicing because the binaries starts with 0b10101

sam = Solution()
Inputa = "1010"
Inputb = "1101"
result = sam.addBinary(Inputa, Inputb)
print(result)
