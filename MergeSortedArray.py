# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 2022

@author: Michael Lin
"""
from typing import List


class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1[p1] > nums2[p2]:
                nums1[p1], nums2[p2] = nums2[p2], nums1[p1]
            p1 += 1
            nums2 = sorted(nums2)

        if nums2:
            nums1[p1:] = nums2[p2:]


class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m-1, n-1
        if p2 >= 0:
            for i in range(len(nums1)-1, -1, -1):

                if nums1[p1] > nums2[p2]:
                    nums1[i] = nums1[p1]
                    p1 -= 1
                elif nums1[p1] <= nums2[p2]:
                    nums1[i] = nums2[p2]
                    p2 -= 1

                if p1 < 0:
                    nums1[:i] = nums2[:p2+1]
                    break
                if p2 < 0:
                    break


# Cleaner implementation of method 2
class Solution3:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while n > 0:
            if m <= 0 or nums2[n-1] > nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
