#!/usr/bin/env python3
"""
determine whether an integer is a palindrome. An integer is a palindrome when
it reads the same backward as forward
Exampple 1:
    Input: 121
    Output: true

Example 2:
    Input: -121
    Output: false
Explanation: From left to right, it reads -121. From right to left,
it becomes 121-. Therefore it is not a palindrome

Example 3:
    Input: 10
    Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome
"""
class Solution():
    def intPalin(self, s : int) -> bool:
       #return(str(s) == str(s)[::-1])

    # Solution for integers not converting to str
        rev_num = 0
        digit = 0

        while (s // 10 ** digit != 0):
            rev_num = (rev_num * 10) + (s // 10 ** digit) // 10
            digit += 1
        return(s == rev_num)


b = Solution()
test = 10
result = b.intPalin(test)
print(result)
