# -*- coding: utf-8 -*-
"""
Created on Sat May 14 2022

@author: Michael Lin
"""
from typing import List


# Pythonic way of solving things
class Solution1:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        res = nums[-k:] + nums[:-k]
        for i in range(len(nums)):
            nums[i] = res[i]


# Need to create new reverse function for this operation
# O(1) memory usage
class Solution2:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse_inplace(nums, 0, len(nums))
        self.reverse_inplace(nums, 0, k)
        self.reverse_inplace(nums, k, len(nums))

    def reverse_inplace(self, nums, start, end):
        for i in range((end - start) // 2):
            nums[start + i], nums[end - 1 - i] = nums[end - 1 - i], nums[start + i]

