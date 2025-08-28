#!/usr/bin/env python3
"""
In this situation, we are given a list of strings, with each string representing a document. Our task is to generate an index of all the distinct words in the documents for quick reference. We need to create a dictionary where each unique word is a key, and the corresponding value is a list of indices pointing to the documents where the word can be found.
"""
from typing import List, Dict


class Solution:
    def keyword_index(self, docs: List[str]) -> Dict[str, List[int]]:
        index: Dict[str, List[int]] = {}

        for doc_idx, doc in enumerate(docs):
            for word in doc.split():
                if word in index:
                    index[word].append(doc_idx)
                else:
                    index[word] = [doc_idx]
        return index


samke = Solution()
Input = ["hello world", "world of python"]
result = samke.keyword_index(Input)
print(result)
