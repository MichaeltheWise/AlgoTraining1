# -*- coding: utf-8 -*-
"""
Created on Tue May 24 2022

@author: Michael Lin
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Create a node as we go along, O(n)
class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return ListNode('')
        elif not head.next:
            return head

        prev, curr = ListNode(head.val), head.next

        while curr.next:
            dummy = ListNode(curr.val)
            dummy.next = prev
            prev = dummy
            curr = curr.next

        curr.next = prev
        return curr


# Directly swap
# First temporarily store the next element, point the current element to previous element
# Assign current element to prev element, temporarily stored next element to current element
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head = prev
        return head


# Non-intuitive recursive method
class Solution3:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Terminal condition: keep going down the list until the next becomes null, then return current position
        # Usually the second-to-last position besides edge case
        if not head:
            return head
        if not head.next:
            return head

        res = self.reverseList(head.next)

        # After second to last position is found, first make a loop, then break the loop by assigning to none
        head.next.next = head
        head.next = None
        return res
