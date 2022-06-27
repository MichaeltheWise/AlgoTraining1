# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 2022

@author: Michael Lin
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


# The most straightforward way is to loop through n
# But the most efficient way is to do binary search O(log(n))
class Solution:
    def firstBadVersion(self, n: int) -> int:
        def check(low, high):
            mid = (low + high) // 2
            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid
            elif isBadVersion(mid):
                return check(low, mid)
            else:
                return check(mid + 1, high)

        return check(0, n)
