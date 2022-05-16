# -*- coding: utf-8 -*-
"""
Created on Mon May 16 2022

@author: Michael Lin
"""
from operator import xor
from typing import List
from functools import reduce


# Use set since we don't need to store in key - value pair
class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        d = set()
        for _ in nums:
            if _ in d:
                d.remove(_)
            else:
                d.add(_)
        return d.pop()


# The fastest way is to use XOR
# If XOR two identical numbers, 0 is returned; otherwise, the missing number
class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)


# Purely arithmetic
class Solution3:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # Also the quickest way to find any missing number from a sorted sequence
        return 2 * sum(set(nums)) - sum(nums)

