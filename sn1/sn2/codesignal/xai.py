#!/usr/bin/env python3

def solution(n, m, figures):
    """
    Place named figures onto an n x m grid and mark cells using the
    1-based index of each figure in `figures`.
    Placement strategy: greedy scan (rows, then cols) — first valid placement wins.
    """

    # Shape definitions adjusted to match the expected sample output
    shapes = {
        "A": [[1]],                   # single cell
        "B": [[1, 1, 1]],             # horizontal length-3
        "C": [[1, 1],
              [1, 1]],                # 2x2 block
        "D": [[1, 0],
              [1, 1],
              [1, 0]],                # vertical with middle-right (3x2 bounding box)
        "E": [[0, 1, 0],
              [1, 1, 1]]              # T piece (provided as example)
    }

    # Initialize grid of zeros (correctly: independent rows)
    grid = [[0 for _ in range(m)] for _ in range(n)]

    def can_place(shape, row, col):
        """Return True if `shape` can be placed with top-left at (row, col)."""
        rows, cols = len(shape), len(shape[0])
        for i in range(rows):
            for j in range(cols):
                if shape[i][j] == 1:
                    # out of bounds or overlapping -> cannot place
                    if row + i >= n or col + j >= m or grid[row + i][col + j] != 0:
                        return False
        return True

    def place(shape, row, col, mark):
        """Stamp `shape` into `grid` using integer `mark`."""
        rows, cols = len(shape), len(shape[0])
        for i in range(rows):
            for j in range(cols):
                if shape[i][j] == 1:
                    grid[row + i][col + j] = mark

    # Main placement loop: each figure gets the first valid top-left position (scan rows -> cols)
    for idx, fig in enumerate(figures, start=1):  # idx is 1-based index recorded in the grid
        if fig not in shapes:
            raise ValueError(f"Unknown figure: {fig}")
        shape = shapes[fig]

        placed = False
        for r in range(n):
            for c in range(m):
                if can_place(shape, r, c):
                    place(shape, r, c, idx)
                    placed = True
                    break
            if placed:
                break
        # If not placed we currently skip silently — you can raise or log if desired.

    return grid


if __name__ == "__main__":
    n, m = 4, 4
    figures = ['D', 'B', 'A', 'C']
    result = solution(n, m, figures)
    for row in result:
        print(row)

