# -*- coding: utf-8 -*-
"""
Created on Sun Jun 5 2022

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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symcheck(left, right):
            if not left and not right:
                return True
            # If left exists but right doesn't
            if left and not right:
                return False
            # If right exists but left doesn't
            if right and not left:
                return False
            if left and right and left.val != right.val:
                return False
            return symcheck(left.left, right.right) and symcheck(left.right, right.left)
        return symcheck(root.left, root.right)


# Iterative
class Solution2:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = [(root.left, root.right)]
        while queue:
            curr = queue.pop()
            if curr[0] and not curr[1]:
                return False
            if not curr[0] and curr[1]:
                return False
            if curr[0] and curr[1] and curr[0].val != curr[1].val:
                return False

            if curr[0] or curr[1]:
                queue.append((curr[0].left, curr[1].right))
                queue.append((curr[0].right, curr[1].left))
        return True
