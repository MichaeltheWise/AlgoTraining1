# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 2022

@author: Michael Lin
"""
from typing import List


# One pass, O(n) space
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')
        res = [0] * (len(prices) + 1)
        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            res[i] = prices[i] - min_val
        return max(res)


# One pass, O(1) space
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        min_val = float('inf')
        max_val = 0
        for i in range(len(prices)):
            if prices[i] < min_val:
                min_val = prices[i]
            max_val = max(max_val, prices[i] - min_val)
        return max_val
