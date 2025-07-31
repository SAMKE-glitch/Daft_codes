#!/usr/bin/env python3
"""
Let's start with an interesting task. Imagine being asked to construct a simple word frequency analyzer. Given a large body of text, we need to identify the three most frequently occurring words. Imagine working with large documents, such as news articles, thesis manuscripts, or even books. Identifying the most common words could give us an overview of the main themes or topics in the text.
"""
from collections import defaultdict


class Solution:
    def frequentWordsFinder(self, text:str) -> int:
        text =text.lower()

        wordCounts = defaultdict(int)

        wordList = text.split()
        for word in wordList:
            wordCounts[word] += 1
        topThree = sorted(wordCounts.items(), key=lambda x: x[1], reverse=True)[:3]
        return topThree

