# -*- coding: utf-8 -*-
"""
Created on Tue May 31 2022

@author: Michael Lin
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Two pointers: one slow and one fast
# Can be used to find midpoint and also cycles
class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast and fast.val == slow.val and fast.next == slow.next:
                return True
        return False


# Make sure everything points to themselves and just do one pass
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = head
        if not p:
            return False

        while p.next:
            nxt = p.next
            if p and nxt.val == p.val and nxt.next == p.next:
                return True
            p.next = p
            p = nxt
        return False


# Pythonic implementation
class Solution3:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        while head:
            if head not in seen:
                seen[head] = 1
            else:
                return True
            head = head.next
        return False
