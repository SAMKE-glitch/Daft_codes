#!/usr/bin/env python3
"""
Your mission is to find the five least common words in a given English text.
The words should be counted case-insensitively and must be separated by single whitespaces.
Assume there is no punctuation. In case there is a tie, 
simply return words in the order they are stored in your dictionary, don't worry about ties!
"""
from collections import defaultdict
from typing import List

class Solution:
    def rare_words_finder(self, text: str) -> List[tuple[str, int]]:
        text = text.lower()

        count_words = defaultdict(int)
        words_list = text.split()

        for word in word_list:
            count_words[word] += 1
        least_five = sorted(count_words.items(), key=lambda x:x[1])[:5]
        return least_five

samke = Solution()
print(samke.rare_words_finder("Hey there hot shot Are you ready for a challenge This might be trickier than it looks"))
