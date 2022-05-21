# -*- coding: utf-8 -*-
"""
Created on Sat May 21 2022

@author: Michael Lin
"""
from typing import List
from itertools import combinations


# Two pass
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target - nums[i]) in nums[i+1:]:
                # Need to adjust for duplicate elements case
                return [i, i + 1 + nums[i+1:].index(target - nums[i])]


# Use dictionary for better access: one pass
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res_dict = {}
        for i, v in enumerate(nums):
            res = target - v
            if res in res_dict:
                return [i, res_dict[res]]
            res_dict[v] = i


# For shorter list
class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        combos = list((i, j) for ((i, _), (j, _)) in combinations(enumerate(nums), 2))
        for combo in combos:
            if nums[combo[0]] + nums[combo[1]] == target:
                return list(combo)
