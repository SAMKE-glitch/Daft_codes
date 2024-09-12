#!/usr/bin/env python3
"""
write a program that converts decimal number to binary
"""
class Solution:
    def decimalBinary(self, n:int) -> str:
        if n == 0:
            return "0"

        binary_number = ""
        while n > 0:
            remainder = n % 2
            binary_number += str(remainder)
            n = n // 2
        return binary_number

if __name__ == "__main__":
    Input = (input("enter number"))
    solution = Solution()
    result = solution.decimalBinary(Input)
    print(result)
