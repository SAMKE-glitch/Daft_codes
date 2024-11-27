#!/usr/bin/env python3
"""
Given a positive integer N, a magical sequence is defined as a sequence of consecutive
integers whose sum is equal to N. You need to return the possible number 
of magical sequences that exist for a given N
Def magicseq(N):
    Input 15
    Output 4
"""
class Solution:
    def magicalSequence(self, N: int) -> int:
        """
        Find the number of magical sequences (consecutive integers) that sum to N.
        Args:
            N (int): The target sum for the sequence.
        Returns:
            int: the count of magical sequences
        """
        # To store the number of sequences
        count = 0

        # Try every possible length of the sequence (k)
        k = 1

        while k * (k -1) // 2 < N:
            # check if there's an integer starting value `a` that works for this length `'`
            remainder = N - (k * (k -1 )) // 2

            # ensure a is an integer
            if remainder % k == 0:
                count += 1

            k += 1
        return count

sam = Solution()
Input = 15
result = sam.magicalSequence(Input)
print(result)
