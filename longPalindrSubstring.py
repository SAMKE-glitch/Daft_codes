#!/usr/bin/env python3
"""
Given a string s, return the longest palindromic substring in s
Example 1:
    Input: s = "babad"
    Output: "bab"
    Note: "aba" is also a valid answer

Example 2:
    Input: s = "cbbd"
    Output: "bb"

Example 3:
    Input: s = "a"
    Output: "a"
Example 4:
    Input: s = "ac"
    Output: "a"

Constraints:
    -> 1 <= s.lenght <= 1000
    -> s Consist of only digits and English letter (lower-case and/or upper-case)
"""
#from Typing import list
class Solution():
    def longestPalindrome(self, s: str) -> str:
        #Helper function for First method to solve the problem

        def check_palin(s:str) -> bool:
            return(s == s[::-1])

        #first solution using for loops or brute force
        for length in range(len(s), 0, -1):
            for start_index in range(0, len(s) + 1 - length):
                if check_palin(s[start_index : start_index + length]):
                    return(s[start_index : start_index + length])
        

        # Second helper function, the most efficient solution and optimized one
        def expand_around_center(self, left:int, right:int) -> str:
            while(left > 0 and right < len(s) and s[left] == s[right]):
                    left -= 1
                    right += 1
            return(s[left + 1: right])

        # handle edge case when no string or single character available
        if not s or len(s) == 1:
            return s

        longest = ""
        # iterate through the len s
        for i in range(len(s)):
            # Handle for odd len
            temp = expand_around_center(i, i)
            if len(temp) > len(longest):
                longest = temp

            #Handle for even len s
            temp = expand_around_center(i, i+1)
            if len(temp) > len(longest):
                longest = temp
        return longest

solution = Solution()
test_case = "babad"
result = solution.longestPalindrome(test_case)
print(result)



