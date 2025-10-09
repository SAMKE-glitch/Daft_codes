#!/usr/bin/env python3
"""
Consider a string, S that is a series of characters, each followed by its frequency
as an integer. The string is not compressed correctly, so there may be multiple
occurrences of the same character. A properly compressed string will consist of one instance
of each character in alphabetical order followed by the total count of that character within the string.
"""

def compress_string(s: str) -> str:
    char_frequency = {}

    # Iterate over the input string two characters at a time
    for i in range(0, len(s), 2):
        char = s[i]  # Character
        freq = int(s[i + 1])  # Frequency (assumes it's always a single digit number)

        # Add frequency to the dictionary (or update if already present)
        if char in char_frequency:
            char_frequency[char] += freq
        else:
            char_frequency[char] = freq

    # Sort characters and create the output string
    compressed_string = ""
    for char in sorted(char_frequency.keys()):
        compressed_string += f"{char}{char_frequency[char]}"

    return compressed_string


if __name__ == "__main__":
    s = input("Enter the string: ")
    result = compress_string(s)
    print(result)
