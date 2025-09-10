#!/usr/bin/env python3
"""
Hey there, I've got a stellar task for you where you gotta be like a cosmic librarian! You know, we got gazillion documents in the universe, each represented as a string in a list. Your task is to whip up an index that's as nifty as a dictionary which logs in every unique word from these documents. Now, don't forget, each unique word is a key, mapping to another dictionary where the key is the document index and the value is how many times that word appeared in the document. It's sure gonna make searching a lot quicker, kinda like quantum speed, eh? Let's get rollin'!

Ensure that your code handles all the edge cases. The input would be a list, where each string inside the list is a document. And every string is just a regular english text, easy peasy.

The output should be a dictionary, where each unique word is a key, and the mapped value should be another dictionary, having document index as the key and its corresponding word count as the value.

Alright, time to hit the hyper-speed!
"""
from collections import defaultdict
from typing import List, Dict



class Solution:
    def keyword_index(self, docs:List[str]) -> Dict[str, Dict[int, int]]:
        index = defaultdict(lambda: defaultdict(int))

        for doc_idx, doc in enumerate(docs):
            for word in doc.split():
                index[word][doc_idx] += 1
        return index


samke = Solution()
docs = ["The fox jumps", "The dog sleeps"]
result = samke.keyword_index(docs)
print(result)
