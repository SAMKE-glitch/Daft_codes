def threeSum(nums):
    """
    Finds all unique triplets in the array `nums` that sum to zero.
    
    Args:
        nums (List[int]): The input array of integers.
        
    Returns:
        List[List[int]]: A list of unique triplets that sum to zero.
    """
    # Step 1: Sort the input array to simplify the process of avoiding duplicates
    nums.sort()  # In-place sorting, modifies the array directly
    result = []  # Initialize an empty list to store the result
    
    # Step 2: Iterate through the array, treating each number as a potential "fixed" number
    for i in range(len(nums) - 2):  # Stop at len(nums) - 2 to leave room for two more elements
        # Skip duplicate fixed elements to avoid duplicate triplets in the result
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Step 3: Use the two-pointer approach to find pairs that sum to the negative of the fixed number
        left = i + 1  # Initialize the left pointer to the element just after nums[i]
        right = len(nums) - 1  # Initialize the right pointer to the last element of the array
        
        # While the left pointer is to the left of the right pointer
        while left < right:
            # Calculate the sum of the triplet
            total = nums[i] + nums[left] + nums[right]
            
            # Case 1: If the sum is zero, we've found a valid triplet
            if total == 0:
                # Add the triplet to the result
                result.append([nums[i], nums[left], nums[right]])
                
                # Move the left pointer to the right past any duplicate elements
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                # Move the right pointer to the left past any duplicate elements
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # Move both pointers inward to search for new pairs
                left += 1
                right -= 1
            
            # Case 2: If the sum is less than zero, we need a larger number
            elif total < 0:
                left += 1  # Move the left pointer to the right to increase the sum
            
            # Case 3: If the sum is greater than zero, we need a smaller number
            else:
                right -= 1  # Move the right pointer to the left to decrease the sum
    
    # Step 4: Return the result list containing all unique triplets
    return result

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]

