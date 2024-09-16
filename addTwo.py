#!/usr/bin/env python3
"""
You are given two non-empty linked lists represents two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two do not contain any leading zero, except for the number 0 itself

Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807
"""
# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # we have to keep track of the final added linked list
        added = ListNode(val = (l1.val + l2.val) % 10) # we use modulus to not get value greter than 9

        # we need to keep track of the carry over number ie greater than 9 if its 10 we need to carry 1
        carry_over = (l1.val + l2.val) // 10
