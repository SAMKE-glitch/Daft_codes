# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Dummy node to simplify the result list manipulation
        dummy = ListNode()
        current = dummy
        carry = 0
        
        # Traverse both linked lists
        while l1 or l2 or carry:
            # Extract values from current nodes, default to 0 if no node
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            new_digit = total % 10
            
            # Create a new node with the digit
            current.next = ListNode(new_digit)
            current = current.next
            
            # Move to the next nodes in the lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next

