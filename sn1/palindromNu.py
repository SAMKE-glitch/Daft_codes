#!/usr/bin/env python3
"""
Determine whether an integer is a palindrome. An integer is a palindrom when
it reads the same backward as forward.

Example 1:
    Input: 121
    Output: true

Example 2:
    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left,
    it becomes 121-, Therefore it is not a palndrome.

Example 3:
    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """x = str(x)
        return(x == x[::-1])
        # we need to declare a variable to store the reversed digits
        rev_digit = 0
        # a variable to store the digit we're looking at
        digit = 0

        while(x // (10**digit) != 0):
            rev_digit = (rev_digit * 10) + (x // (10**digit) % 10)
            digit += 1
        return(x == rev_digit)"""
        # Early exit for negative numbers and numbers ending with 0 (except 0 itself)
        if x < 0 or (x % 10 == 0 and x !=0):
            return False

        original = x # store the orginal number to compare later
        rev_digit = 0

        while x > 0:
            rev_digit = rev_digit * 10 + x % 10 # Extract the last digit of x and add it to rev_digit
            x //= 10 # Remove the last digit from x
        return original == rev_digit


sam = Solution()
Enput = 121
result = sam.isPalindrome(Enput)
print(result)
