#!/usr/bin/env python3
"""
FizzBuzz question
"""
class Solution:
    def fizzBuzz(self, n: int) -> str:
        for i in range(1, n+1):
            if (i % 3 == 0) and (i % 5 == 0):
                print("FizzBuzz")
            elif i % 3 == 0 and i % 5 != 0:
                print("Fuzz")
            elif i % 5 == 0 and i % 3 != 0:
                print("Buzz")
            else:
                print("{}".format(i))

