# -*- coding: utf-8 -*-
"""
Created on Thu May 26 2022

@author: Michael Lin
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Pythonic implementation, O(n) run time but with O(n) space
class Solution1:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res == res[::-1]


# Can use two pointers method but need to reverse the list first from midpoint and find midpoint
# This is O(n) and space O(1)
class Solution2:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.midPoint(head)
        mid_reverse = self.reverseList(mid)
        start, end = head, mid_reverse
        while end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.next
        return True

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head = prev
        return head

    def midPoint(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow