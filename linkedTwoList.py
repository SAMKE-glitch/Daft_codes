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
        # we need to declare our variable to store the added values
        added = ListNode(val = (l1.val + l2.val) % 10)
        # we need to take care of the carried over number to the next node
        carry_over = (l1.val + l2.val) // 10
        # declare a current node to track the operation we are doing
        current_node = added

        while(l1.next and l2.next):
            l1 = l1.next
            l2 = l2.next

            current_node.next = ListNode(val = (carry_over + l1.val + l2.val) % 10)
            carry_over = (carry_over + l1.val + l2.val) // 10
            current_node = current_node.next
        # now we I need to take care when one list node is longer than the other
        while(l1.next):
            l1 = l1.next

            current_node.next = ListNode(val = (carry_over + l1.val) % 10)
            carry_over = (carry_over + l1.val) // 10
            current_node = current_node.next
        # do the same for l2 
        while(l2.next):
            l2 = l2.next

            current_node.next = ListNode(val = (carry_over + l2.val) % 10)
            carry_over = (carry_over + l2.val) // 10
            current_node = current_node.next

        if (carry_over) > 0:
            current_node.next = ListNode(val = 1)

        return added

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
