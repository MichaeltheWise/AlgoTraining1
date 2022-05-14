# -*- coding: utf-8 -*-
"""
Created on Sat May 14 2022

@author: Michael Lin
"""
from typing import List


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


# Update the previous value to potentially be faster though same time complexity
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        profit, prev = 0, prices[0]
        for v in prices:
            if v - prev > 0:
                profit += v - prev
            prev = v
        return profit
