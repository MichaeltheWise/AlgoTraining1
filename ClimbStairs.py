# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 2022

@author: Michael Lin
"""


# Time limit exceeded but correct answers
class Solution1:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 0:
            return 1
        return self.climbStairs(n-2) + self.climbStairs(n-1)


# Iteration
class Solution2:
    def climbStairs(self, n: int) -> int:
        res = [0] * (n+1)
        res[0], res[1] = 1, 2
        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]
        return res[n-1]