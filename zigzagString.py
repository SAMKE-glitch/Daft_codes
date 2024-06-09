#!/usr/bin/env python3
"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given 
number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion
given a number of rows:
    string convert(string s, int numRows);

Example 1:
    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
Example 2:
    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:
    P     I     N
    A   L S   I G 
    Y A   H R
    P     I

Example 3:
    Input: s = "A", numRows = 1
    Output: "A"

"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        row_map = {row:"" for row in range(1, numRows+1)}

        row = 1
        up = True

        for letter in s:
            row_map[row] += letter
            if (row == 1) or ((row < numRows) and up):
                row += 1
                up = True
            else:
                row -= 1
                up = False
        coverted = ""

        for row in range(1, numRows+1):
            converted += row_map[row]
        return converted

