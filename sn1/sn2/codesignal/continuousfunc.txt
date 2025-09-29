#!/usr/bin/env python3
"""
Bravo, Voyager! You have successfully traversed the fascinating cosmos of binary searches on continuous functions. However, a space probe indicates that there might be situations where we need to identify a specific target value instead of finding a function's zero.
We should modify our current code to determine 
x when f(x) = 50 for the function f(x) = x^4 - x^2 -10, on the interval [-5, 5]
"""
# Python program to find the root of a given function using Binary Search
import math
import numpy as np

# Define a continuous function 'f' where f(x) = x^4 - x^2 - 10
def f(x):
    return x**4 - x**2 - 10

# Define the binary search function 
def binary_search(func, target, left, right, precision):
    while np.abs(func(left)) > precision and np.abs(func(right)) > precision:
        middle = (left + right) / 2
        if func(middle) < target:
            left = middle
        else:
            right = middle
            
    return middle

epsilon = 1e-6  # to make sure the solution is within an acceptable range
target = 0  # target value for root of function 'f'
start = -5  # starting point of the interval
end = 5  # ending point of the interval

result = binary_search(f, target, start, end, epsilon)
print("The value of x for which f(x) is approximately 0 within the interval [" + str(start) + ", " + str(end) + "] is: ", result)
