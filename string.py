def count_substrings(s):
  """
  This function counts the number of substrings in a string.

  Args:
      s: The string to count substrings from.

  Returns:
      The number of substrings in the string.
  """
  n = len(s)
  # Count the number of substrings starting at each index
  count = n
  for i in range(n):
    # Add the length of each substring starting at index i
    count += i
  return count
