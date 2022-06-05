# -*- coding: utf-8 -*-
"""
Created on Sun Jun 5 2022

@author: Michael Lin
"""
from typing import Optional, List
from collections import deque, defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative
class Solution1:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue, d = [(0, root)], {}
        while queue:
            curr = queue.pop()
            lvl = curr[0]
            if curr[1]:
                if lvl in d:
                    d[lvl].append(curr[1].val)
                else:
                    d[lvl] = [curr[1].val]

                queue.append((lvl + 1, curr[1].right))
                queue.append((lvl + 1, curr[1].left))
        return list(d.values())


# Iterative without dictionary
class Solution2:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        dq = deque()
        dq.append(root)

        while dq:
            length = len(dq)
            curr = []
            for _ in range(length):
                node = dq.popleft()
                curr.append(node.val)

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(curr)
        return res


# Recursion
class Solution3:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def traverse(root, level, res):
            if root:
                if level in res:
                    res[level].append(root.val)
                else:
                    res[level] = [root.val]
                traverse(root.left, level+1, res)
                traverse(root.right, level+1, res)
        res = {}
        traverse(root, 0, res)
        return list(res.values())


# Can move the result outside of the function
class Solution4:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)
        if not root:
            return res.values()

        def traverse(node, level):
            res[level].append(node.val)
            if node.left:
                traverse(node.left, level+1)
            if node.right:
                traverse(node.right, level+1)

        traverse(root, 0)
        return res.values()
