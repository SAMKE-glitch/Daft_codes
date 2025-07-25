#!/usr/bin/env python3
"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node
Note: A leaf is anode with no children.

Example:
    Given binary tree [3, 9, 20, null, null, 15, 7],
    
    return its depth = 3
"""
# Defination for a binary tree node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # If we are given an emoty root node then our return is zero
        if not root:
            return 0
        return(1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))
