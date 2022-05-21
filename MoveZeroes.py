# -*- coding: utf-8 -*-
"""
Created on Sat May 21 2022

@author: Michael Lin
"""
from typing import List


class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, 1
        while p1 < len(nums) and p2 < len(nums):
            # Three cases:
            # Case 1: number 1 is 0 and number 2 is not 0
            # Case 2: number 1 is 0 and number 2 is 0
            # Case 3: number 1 is 1
            if nums[p1] == 0 and nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1
            elif nums[p1] != 0:
                p1 += 1
            p2 += 1


# Trying to replace directly
class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_index, nonzero_index = [], []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_index.append(i)
            else:
                nonzero_index.append(i)

        if len(nums) == 1 or not nonzero_index:
            # Don't do any calculation, jump out
            return None

        nonzero_index.extend(zero_index)
        for i in range(len(nonzero_index)):
            nums[i], nonzero_index[i] = nums[nonzero_index[i]] if i <= nonzero_index[i] else nonzero_index[
                nonzero_index[i]], nums[i]


# Use one pointer: easiest way
class Solution3:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[p] = nums[i]
                p += 1

        for i in range(p, len(nums)):
            nums[i] = 0


