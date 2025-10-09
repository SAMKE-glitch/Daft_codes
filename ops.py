#!/usr/bin/env python3
"""
calPoints
"""
def calPoints(ops) -> int:
    stack = []
    result = None
    for op in ops:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "C":
            stack.pop()
        elif op == "D":
            stack.append(2 * stack[-1])
        else:
            stack.append(int(op))
    result = sum(stack)
    return result

if __name__ == "__main__":
    ops1 = ["5", "-2", "4", "C", "D", "9", "+", "+"]
    print(calPoints(ops1))
