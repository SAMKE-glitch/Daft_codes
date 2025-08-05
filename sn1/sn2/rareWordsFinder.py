#!/usr/bin/env python3
"""
Your mission is to find the five least common words in a given English text.
The words should be counted case-insensitively and must be separated by single whitespaces.
Assume there is no punctuation. In case there is a tie, 
simply return words in the order they are stored in your dictionary, don't worry about ties!
"""
from collections import defaultdict

class Solution:
    def rare_words_finder(self, text: str) -> List[Tuple[str, int]]:

