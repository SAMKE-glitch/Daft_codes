#!/usr/bin/env python3
"""
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes contain a single
digit. Add the two numbers and return it as a linked list.
you may assume the two numbers do not contain any leading zero,
except for the number 0 itself.
Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807
"""
# Defination for singly-linled list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:



# Create the first linked list representing the number 342
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)


# Create the second linked list representing the number 465
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


solution = Solution()
result = solution.addTwoNumbers(l1, l2)

while result:

    print(result.val, end=" -> ")
    result = result.next
