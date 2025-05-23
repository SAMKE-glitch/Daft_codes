#!/usr/bin/env python3

def solution(s: str) -> int:
    n = len(s)
    circular_s = s + s  # Concatenate the string with itself to handle circular substrings
    substrings = set()

    # Generate all circular substrings of original length `n`
    for i in range(n):
        for length in range(1, n + 1):
            # Take substring of the required length starting from `i`
            substrings.add(circular_s[i:i + length])

    # Count unique substrings
    return len(substrings)

# Test the function with the example input
print(solution("CCB"))  # Output should be 8

