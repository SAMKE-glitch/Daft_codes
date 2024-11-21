#!/usr/bin/env python3

def getMinNumber(text, search, wholeWord, start):
    # Check if `wholeWord` is 'Y' or 'N'
    is_whole_word = (wholeWord == 'Y')
    
    # Start searching from the given index
    pos = start

    while pos < len(text):
        # Find the next occurrence of `search` starting from `pos`
        pos = text.find(search, pos)
        if pos == -1:  # If no occurrence is found, break the loop
            break
        
        # If `wholeWord` is 'Y', validate whole-word conditions
        if is_whole_word:
            # Check left boundary: Start of string or preceded by space
            left_valid = (pos == 0 or text[pos - 1] == ' ')
            # Check right boundary: End of string or followed by space
            right_valid = (pos + len(search) == len(text) or text[pos + len(search)] == ' ')
            # If both conditions are valid, return the position
            if left_valid and right_valid:
                return pos
        else:
            # If `wholeWord` is 'N', return the position as soon as it's found
            return pos
        
        # Move `pos` forward to search for the next occurrence
        pos += 1

    # If no valid occurrence is found, return "Goodbye Watson"
    return "Goodbye Watson"

# Input and Output
T = int(input())  # Number of test cases
for _ in range(T):
    text = input()  # Sentence S1
    search = input()  # String S2
    wholeWord = input()  # Character C ('Y' or 'N')
    start = int(input())  # Starting index I

    # Call the function and print the result
    result = getMinNumber(text, search, wholeWord, start)
    print(result)

