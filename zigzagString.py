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

        # declare a dict variable to store the zigzag rows of strings
        dict_s = {row:"" for row in range(1, numRows + 1)}
        row = 1
        up = True

        # iterate through the string s to get each letter
        for letter in s:
            dict_s[row] += letter
            if (numRows == 1) or ((row < numRows) and up):
                row += 1
                up = True
            else:
                row -= 1
                up = False
        # we have our converted string
        converted = ""
        for row in range(1, numRows + 1):
            converted += dict_s[row]
        return converted

sam = Solution()
a = "PAYPALISHIRING"
num = 4
result = sam.convert(a, num)
print(result)
