#!/usr/bin/env python3
"""
Roman numerals are represemted by seven different symbols:
I, V, X, L, C, D and M.
symbol Value
I       1
V       5
X       10
L       50
C       100
D       500
M       1000
For example, 2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, 
which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However
the numeral for four is not IIII. Instead, the number four is written as IV.
Because the one is before the five we subtract it making four. The same principle
applies to the number nine, which is written as IX. there are six instances where 
subtraction is used:
    I can be place before V (5) and X (10) to make 4 and 9
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be place before D (500) AND M(1000) to make 400 and 900.
Given a roman numeral convert it to an integer

Example 1:
    Input: s = "III"
    Output: 3
Example 2:
    Input: s = "IV"
    Output: 4
Example 3:
    Input: s = "IX"
    Output: 9
Example 4:
    Input: s = "LVIII"
    Output: 58
    Explanation: L = 50, V = 5, III = 3
Example 5:
    Input: s = "MCMXCIV"
    Output: 1994
    Explanation: M = 1000, CM = 900, XC = 90 and IV = 4

Constraints:
    1 <= s.length <= 15
    s contains only characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
    It is guranteed that s is aa valid roman numeral in the range [1, 3999]
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_table = {"I": 1,
                       "V": 5,
                       "X": 10,
                       "L": 50,
                       "C": 100,
                       "D": 500,
                       "M": 1000}
        # String conversion method
        convert = {"IV": "IIII", "IX": "VIIII", "XL": "XXXX",
                    "XC": "LXXXX", "CD": "CCCC", "CM": "DCCCC"}
        # iterate through convert dict
        for k, v in convert.items():
            #replace string in s
            s = s.replace(k, v)
        return sum(roman_table[numeral] for numeral in s)
        # Reverse iteration solution
        # variable to hold total number converted
        num = 0
        # variable to hold last seen character in that string
        last = "I"

        # for loop iterating the string in reverse
        for numeral in s[::-1]:
            # handle the edge case if current numeral is less than last
            if roman_table[numeral] < roman_table[last]:
                num -= roman_table[numeral]
            else:
                num += roman_table[numeral]
            last = numeral
        return num

sam = Solution()
a = "MCMXCIV"
result = sam.romanToInt(a)
print(result)
