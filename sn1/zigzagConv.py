#!/usr/bin/env python3
"""
The string "PAYPALISHIRING" is written in a zigzag patter on a given number of rows
like this: (you may want to display this patter in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R

And then read line by line "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
    string convert(string s, int numRows);

Example 1:
    Input s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

Example 2:
    Input s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explantion:
    
    P   I    N
    A  LS  I G
    Y A H R
    P   I

Example 3:
    Input: s = "A", numRows = 1
    Output: "A"

Constraints:
    -> 1 <= s.length <= 1000
    -> s consists of English letters (lower-case and upper-case), ',' and '.'
    -> 1 <= numRows <= 1000
"""
class Solutiom:
    def convert(self, s:str, numRows: int) -> str:
        # handle if the number of rows equal 1
        if numRows == 1:
            return s
        # declaring the dictionary with row numbers being as keys
        row_map = {row:"" for row in range(1, numRows+1)}

        # declare the row that will start looking at
        row = 1

        # we have to keep in track if we are currently up or down in the zigzag
        up = True

        for letter in s:
            row_map[row] += letter
            if (row == 1) or ((row < numRows) and up):
                row += 1
                up = True
            else:
                row -= 1
                up = False
        converted = ""
        # loop through the numRows in the dictionary
        for row in range(1, numRows+1):
            converted += row_map[row]
        return converted
