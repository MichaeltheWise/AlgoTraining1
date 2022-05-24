# -*- coding: utf-8 -*-
"""
Created on Mon May 23 2022

@author: Michael Lin
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val, node.next = node.next.val, node.next.next


class Solution2:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node and node.next:
            node.val = node.next.val
            prev = node
            node = node.next

        prev.next = None
