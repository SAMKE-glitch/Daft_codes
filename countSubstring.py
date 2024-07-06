def count_substrings(s: str) -> int:
    n = len(s)
    substrings = []
    
    # Generate all substrings
    for start in range(n):
        for end in range(start + 1, n + 1):
            substring = s[start:end]
            if substring not in substrings:
                substrings.append(substring)
    
    # Return the count of substrings
    print(substrings)

# Example usage:
if __name__ == "__main__":
    input_str = "CCB"
    output = count_substrings(input_str)
    print(f"Number of substrings in '{input_str}' is: {output}")

