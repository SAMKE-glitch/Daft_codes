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
class Solution:
    def convert(self, s:str, numRows: int) -> str:
        # handling edge case where numRows = 1
        if numRows == 1:
            return s

        # we need to declare a dict variable to hold num of rows togehter with their strings
        map_dict = {row:"" for row in range(1, numRows+1)}

        # variable to update us which row we are
        row = 1

        # variable to show us whether we are going up or down it has to be a boolean
        up = True

        for letter in s:
            map_dict[row] += letter
            # check if row < numRows and up = True or 
            if (row == 1) or ((row < numRows) and up):
                row += 1
                up = True
            else:
                row -= 1
                up = False

        # our converted or combined string after conversion
        converted = ""
        for row in range(1, numRows+1):
            converted += map_dict[row]
        return converted


sam = Solution()
string = "PAYPALISHIRING"
numrows = 3
result = sam.convert(string, numrows)
print(result)
