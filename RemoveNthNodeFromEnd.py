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


class Solution1:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, count, number, start = head, 1, [head.val], head
        # Count through the linked list
        while curr.next is not None:
            curr = curr.next
            number.append(curr.val)
            count += 1

        # If length equals to desired location, pop first item
        if count == n:
            head = head.next
            return head

        # While not equal, go down the list
        while (count - 1) != n:
            head = head.next
            count -= 1

        # Replace
        head.next = head.next.next
        return start


# Clean up and more efficient
class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count, curr = 0, head
        # Count through the linked list
        while curr:
            count += 1
            curr = curr.next

        # If length equals to desired location, pop first item
        if n == count:
            head = head.next
        else:
            # Go down list
            curr = head
            for i in range(count - n - 1):
                curr = curr.next
            curr.next = curr.next.next
        return head


# Another way to do it
class Solution3:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create an extra node
        dummy = ListNode(0)
        # Extend dummy
        dummy.next = head

        first, second = dummy, dummy

        # Find the first location to extract the second location
        for _ in range(n):
            first = first.next

        # Use first to find the right second location
        while first.next:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next
