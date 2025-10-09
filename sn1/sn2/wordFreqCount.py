#!/usr/bin/env python3

import string

class Solution:
    """
    Solution class to provide dictionary-based utility functions.
    This includes analyzing text data to find the most frequent words.
    """

    def __init__(self, text):
        """
        Initializes the Solution instance with the input text.

        :param text: The body of text to analyze.
        """
        self.text = text.lower().translate(str.maketrans('', '', string.punctuation))

    def find_top_three_words(self):
        """
        Analyzes the initialized text to find the top 3 most frequent words.

        :return: A list of tuples containing the top 3 words and their frequency counts.
        """
        words = self.text.split()
        word_freq = {}

        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return sorted_words[:3]

# Example usage
if __name__ == "__main__":
    sample_text = """
    Python is great for data analysis. Python is used in machine learning, data science, and web development.
    This makes Python one of the most popular languages. Python is easy to learn.
    """
    solution = Solution(sample_text)
    top_words = solution.find_top_three_words()

    for word, count in top_words:
        print(f"'{word}' appears {count} times")

