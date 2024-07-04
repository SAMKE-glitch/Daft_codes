#!/usr/bin/env python3
"""
calPoints
"""
def calPoints(ops) -> int:
    stack = []
    for op in ops:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "C":
            stack.pop()
        elif op == "D":
            stack.append(2 * stack[-1])
        else:
            stack.append(int(op))
    return sum(stack)

if __name__ == "__main__":
    ops1 = ["5", "2", "C", "D", "+"]
    print(calPoints(ops1))
