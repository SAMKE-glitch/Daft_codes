class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def reverseTheLine(self, head):
        prev = None
        current = head
        
        while current is not None:
            next_node = current.next  # Save next node
            current.next = prev       # Reverse the link
            prev = current            # Move prev and current one step forward
            current = next_node       # Move to the next node
        
        return prev  # 'prev' will be the new head after the list is reversed

