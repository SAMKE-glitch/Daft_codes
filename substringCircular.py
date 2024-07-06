def solution(s: str) -> int:
    n = len(s)
    circular_s = s + s  # Concatenate the string with itself
    substrings = set()
    
    # Generate all circular substrings
    for i in range(n):
        for length in range(1, n + 1):
            substrings.add(circular_s[i:i + length])
    
    # Count unique substrings
    return len(substrings)

# Test the function with the example input
print(solution("BCC"))  # Output should be 8

