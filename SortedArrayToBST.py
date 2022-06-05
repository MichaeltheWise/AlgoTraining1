# -*- coding: utf-8 -*-
"""
Created on Sun Jun 5 2022

@author: Michael Lin
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Recursion
class Solution1:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(partial_list):
            if not partial_list:
                return
            midpoint = len(partial_list)//2
            tree = TreeNode(partial_list[midpoint])
            tree.left = construct(partial_list[:midpoint])
            tree.right = construct(partial_list[midpoint+1:])
            return tree
        return construct(nums)


# Use the function directly
class Solution2:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0])
        elif len(nums) == 0:
            return None

        midpoint = len(nums) // 2
        node = TreeNode(nums[midpoint])
        node.left = self.sortedArrayToBST(nums[:midpoint])
        node.right = self.sortedArrayToBST(nums[midpoint+1:])
        return node


# Iterative
class Solution3:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        queue = [(root, nums, 0)]
        while queue:
            prev, partial_list, lr = queue.pop(0)
            if partial_list:
                mid = len(partial_list) // 2
                node = TreeNode(partial_list[mid])
                if lr:
                    prev.right = node
                else:
                    prev.left = node

                queue.append((node, partial_list[:mid], 0))
                queue.append((node, partial_list[mid + 1:], 1))
        return root.left
