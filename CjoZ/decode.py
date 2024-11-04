import requests

def decode_secret_message(doc_url):
    # Fetch the document data
    response = requests.get(doc_url)
    response.raise_for_status()  # Ensure we got a successful response

    # Split the content into lines for processing
    lines = response.text.strip().splitlines()

    # Parse the characters and their coordinates
    grid = {}
    max_x = 0
    max_y = 0

    for line in lines:
        print(f"Processing line: '{line}'")  # Debug output
        if line.strip():  # Ensure the line is not empty
            parts = line.split(',')
            if len(parts) == 3:  # Check if we have exactly 3 parts
                char = parts[0].strip()  # Character
                x_str = parts[1].strip()  # x-coordinate
                y_str = parts[2].strip()  # y-coordinate
                
                try:
                    x = int(x_str)  # Convert x-coordinate to integer
                    y = int(y_str)  # Convert y-coordinate to integer

                    # Store the character at its grid position
                    grid[(x, y)] = char

                    # Track the maximum coordinates for grid dimensions
                    max_x = max(max_x, x)
                    max_y = max(max_y, y)

                except ValueError:
                    print(f"Invalid coordinate values in line: '{line}'")
            else:
                print(f"Line skipped due to incorrect format: '{line}'")
        else:
            print("Empty line detected.")

    # Create the 2D grid with spaces
    grid_output = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    # Fill the grid with characters
    for (x, y), char in grid.items():
        grid_output[y][x] = char  # y is the row (height), x is the column (width)

    # Print the grid
    for row in grid_output:
        print(''.join(row))

# Example usage (insert a valid Google Doc URL here)
decode_secret_message('https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub')

