# -*- coding: utf-8 -*-
"""
Created on Mon May 16 2022

@author: Michael Lin
"""
from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Swap order of list
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        res = []
        for v in nums1:
            if v in nums2:
                res.append(nums2.pop(nums2.index(v)))
        return res


# If array sorted
class Solution2:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1, nums2, p1, p2, res = sorted(nums1), sorted(nums2), 0, 0, []

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        while 0 <= p1 < len(nums1) and 0 <= p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
                p2 += 1
            # Always increment the smaller one
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return res


# Use dictionary to be faster
class Solution3:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d, res = {}, []
        for v in nums1:
            if v in d:
                d[v] += 1
            else:
                d[v] = 1

        for u in nums2:
            if u in d and d[u] > 0:
                d[u] -= 1
                res.append(u)
        return res


# Use collection's Counter
class Solution4:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        res = []
        for num in counter1:
            for _ in range(min(counter1[num], counter2[num])):
                # Based on how many counts of a number, append how many times
                res.append(num)
        return res