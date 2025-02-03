#!/usr/bin/env python3
"""
Given a binary tree, find its maximum depth.
The maxima depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

Note: A leaf is a node with no children

Example:
    Given binary tree [2,9, null, null, 15, 7]

    return its depth = 3
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root:TreeNode) -> int:
        if not root:
            return 0
        return(1 + max(self.maxDepth(root.left), self.maxDepth(root.right)))


root = TreeNode(2)
root.left = TreeNode(9)
root.right = TreeNode(15)
root.right.left = TreeNode(7)


sam = Solution()
result = sam.maxDepth(root)
print(result)
