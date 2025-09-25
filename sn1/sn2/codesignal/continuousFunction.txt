#!/usr/bin/env python3
"""
Well done, Space Voyager! You are ready to test your binary search skills in a thrilling, practical scenario.

Imagine that you're watching a ball falling from a building that is 100m high, and you are wondering how long it will take to hit the ground. Thanks to your coding prowess and understanding of the binary search on continuous functions, you can calculate this time precisely.

Let's run the code and see the magic unfold right before your eyes!
"""
# Python program to calculate the point at which a ball dropped from a height h reaches the ground 
# using Binary Search on the continuous function h(t) = h - (1/2) * g * t^2.

import math

# Define the continuous function for the height of the ball at time t 
def h(t, initial_height, g):
    return initial_height - (0.5) * g * t**2

# Define the binary search function
def binary_search(func, initial_height, g, target, left, right, precision):
    while right - left > precision:
        mid = (left + right) / 2
        if func(mid, initial_height, g) < target:
            right = mid
        else:
            left = mid
    return (left + right) / 2

# Requested precision
epsilon = 1e-6
# Constants
initial_height = 100  # Initial height in meters
g = 9.81  # acceleration due to gravity

# Time range 
time_range = [0, 10]

# Call binary_search for h with the target being 0, indicating the hit of the ground
result = binary_search(h, initial_height, g, 0, time_range[0], time_range[1], epsilon)

print("Time when the ball hits the ground (seconds): ", result)
