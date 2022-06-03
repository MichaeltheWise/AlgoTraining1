# -*- coding: utf-8 -*-
"""
Created on Thu Jun 2 2022

@author: Michael Lin
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursion
class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
        # Can also be written as: max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


# Iterative
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            queue = [(root, 1)]

        max_val = float('-inf')
        while queue:
            curr = queue.pop()
            if curr:
                max_val = max(max_val, curr[1])
                if curr[0].left:
                    queue.append((curr[0].left, curr[1] + 1))
                if curr[0].right:
                    queue.append((curr[0].right, curr[1] + 1))
        return max_val


