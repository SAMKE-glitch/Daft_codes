#!/usr/bin/env python3
"""
Alright, ready for the next galaxy-level challenge? Here it is, hot off the spaceship!

Let's imagine you've discovered a list of intergalactic treasures represented by integers in an array arr. Now, you've got a peculiar rule out here in the cosmos: you can only pick up the treasures located at the even indexes in that array! Now, being a smart space explorer, you want to find out the net worth of all these even-indexed treasures.

So, here's your mission: craft a Python function recursiveSumEven that accepts your list-of-integers treasure array as a parameter and returns the sum of all those even-indexed treasures. And since this is the cosmos and peculiar rules rule, you'll need to calculate this sum recursively!

This function will be tested with different-sized lists, including ones with 0 elements, so do consider the edge cases! Sail high, space champion! Remember, the answer is always in the journey.
"""
from typing import List



class Solution:
    def recursiveSumEven(self, arr:List[int], idx=0) -> int:
        if idx >= len(arr):
            return 0

        if idx % 2 == 0:
            return arr[idx] + self.recursiveSumEven(arr, idx+1)
        else:
            return self.recursiveSumEven(arr, idx+1)
