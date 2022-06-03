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

# Original wrong implementation
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True
#         if root.right.val < root.val:
#             return False
#         if root.left.val > root.val:
#             return False
#         return self.isValidBST(root.left) and self.isValidBST(root.right)


# Recursion: need to capture minimum and maximum
class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, l=float('-inf'), r=float('inf')):
            if not node:
                return True
            if l < node.val < r:
                # Need to be between minimum and maximum
                return validate(node.left, l, node.val) and validate(node.right, node.val, r)
            else:
                return False
        return validate(root)


# Iterative
class Solution2:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        queue = [(float('-inf'), root, float('inf'))]
        while queue:
            curr = queue.pop()
            if curr[0] < curr[1].val < curr[2]:
                if curr[1].left:
                    queue.append((curr[0], curr[1].left, curr[1].val))
                if curr[1].right:
                    queue.append((curr[1].val, curr[1].right, curr[2]))
            else:
                return False
        return True
