# -*- coding: utf-8 -*-
"""
Created on Mon May 16 2022

@author: Michael Lin
"""
from typing import List


# Pythonic implementation
class Solution1:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# Use dictionary to be faster
class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for _ in nums:
            if _ not in d:
                d[_] = 0
            else:
                return True
        return False


# Use set: since values are not being stored here, using a set / hash table is much better
class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = set()
        for _ in nums:
            if _ in d:
                return True
            d.add(_)
        return False
