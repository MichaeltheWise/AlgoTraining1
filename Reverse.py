# -*- coding: utf-8 -*-
"""
Created on Sun May 22 2022

@author: Michael Lin
"""


class Solution1:
    def reverse(self, x: int) -> int:
        res = '' if x > 0 else '-'
        for v in str(abs(x))[::-1]:
            res += v

        try:
            # Check if in range to prevent overflow
            if (-2 ** 31) <= int(res) <= (2 ** 31 - 1):
                return int(res)
            else:
                return 0
        except Exception as e:
            return 0


class Solution2:
    def reverse(self, x: int) -> int:
        l, res = [], 0
        neg_flag = 1 if x < 0 else 0
        x = abs(x)
        while x > 0:
            c = x % 10
            l.append(c)
            x = x // 10

        for i in range(len(l)):
            res += l[-(i + 1)] * (10 ** i)
            if res >= 2 ** 31 - 1:
                return 0
        return res if not neg_flag else -res
