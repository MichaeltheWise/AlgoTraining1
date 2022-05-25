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


# Best solution
class Solution1:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res, p1, p2 = ListNode(), list1, list2
        head = res
        while p1 and p2:
            if p1.val > p2.val:
                res.next = p2
                p2 = p2.next
            else:
                res.next = p1
                p1 = p1.next
            res = res.next
        if p1:
            res.next = p1
        if p2:
            res.next = p2
        return head.next


# Horrible solution that doesn't actually use the property of linked list
# It loops through O(n + m) and use an additional O(n + m) space with the next object
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return

        lis = []
        first = list1
        # Loop through the first linked list
        while first:
            lis.append(first.val)
            first = first.next

        # Loop through the second linked list
        sec = list2
        while sec:
            lis.append(sec.val)
            sec = sec.next

        # Sort the combined list
        lis.sort()

        # Create a brand new list to capture this
        temp = head = ListNode(lis[0])
        for ele in lis[1:]:
            x = ListNode(ele)
            temp.next = x
            temp = temp.next

        return head
