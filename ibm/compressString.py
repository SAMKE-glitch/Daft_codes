#!/usr/bin/env python3
"""
Consider a string, S that is a series of characters, each followed by its frequency
as an integer. The string is not compressed correctly, so there may be multiple
occurrences of the same character. A properly compressed string will consist of one instance
of each character in alphabetical order followed by the total count of that character within the string.
"""
class Solution:
    def stringFreq(self, S: str) -> str:
        #0 I need to declare an empty dictionary to store char and its frequency
        #1 iterate the string and pick each character with its subsequent freq and store them to a dictionary
        #2 so we need to obtin these value from the string and then able to store them to the dictionary
        dictionary_freq = {}
        for i in range(0, len(S), 2):
            char = S[i]
            freq = int(S[i+1])

            # add the char and freq to the dictionary
            if char in dictionary_freq:
                dictionary_freq[char] += freq
            else:
                dictionary_freq[char] = freq

        # sort the char in the dictionary
        compressed_string = ""
        for char in sorted(dictionary_freq.keys()):
            compressed_string += f"{char}{dictionary_freq[char]}"
        return compressed_string

if __name__ =="__main__":
    solution = Solution()
    result = solution.stringFreq("a2b1c5a3")
    print(result)
