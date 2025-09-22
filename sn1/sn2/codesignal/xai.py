#!/usr/bin/env python3


def solution(n, m, figures):
    # Define the figure shapes (classic Tetris blocks)
    shapes = {
        "A": [[1, 1, 1, 1]],               # I piece
        "B": [[1, 1],
              [1, 1]],                     # O piece
        "C": [[1, 0, 0],
              [1, 1, 1]],                  # J piece
        "D": [[0, 0, 1],
              [1, 1, 1]],                  # L piece
        "E": [[0, 1, 0],
              [1, 1, 1]]                   # T piece
    }

    # Initialize n x m grid of zeros
    grid = [[0 for _ in range(m)] for _ in range(n)]

    # Place each figure in sequence (top-left alignment for simplicity)
    for idx, fig in enumerate(figures, start=1):  # idx = 1-based index
        shape = shapes[fig]
        rows, cols = len(shape), len(shape[0])

        # Place shape starting at top-left (0,0) → you can change placement logic
        for i in range(rows):
            for j in range(cols):
                if shape[i][j] == 1:
                    grid[i][j] = idx

    return grid


n, m = 4, 4
figures = ['D','B','A','C']
print(solution(n, m, figures))
