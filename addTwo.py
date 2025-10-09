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

        # we need to keep track on the node we current look at i
        current_node = added

        # while loop as long as there is next nodes in both l1 and l2
        while(l1.next and l2.next):
            l1 = l1.next
            l2 = l2.next
            current_node.next = ListNode(val = (carry_over + l1.val + l2.val) % 10)
            carry_over = (carry_over + l1.val + l2.val) // 10

            # then update our current node
            current_node = current_node.next
        # so there might be only value in one node only like l1 = 2345 l2 = 345
        while(l1.next):
            l1 = l1.next
            current_node.next = ListNode(val = (carry_over + l1.val) % 10)
            carry_over = (carry_over + l1.val) // 10
            current_node = current_node.next

        # same if l2 value is only available
        while(l2.next):
            l2 = l2.next
            current_node.next = ListNode(val = (carry_over + l2.val) % 10)
            carry_over = (carry_over + l2.val) // 10
            current_node = current_node.next

        # accounting for the next 1 on the carry over value
        if (carry_over) > 0:
            current_node.next = ListNode(val= 1)
        
        #finally return added ListNode
        return added

