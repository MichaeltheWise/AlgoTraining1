# -*- coding: utf-8 -*-
"""
Created on Sun May 22 2022

@author: Michael Lin
"""
from collections import Counter


class Solution1:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, v in enumerate(s):
            if v not in d:
                d[v] = 1
            else:
                d[v] += 1

        res = float('inf')
        for k, v in d.items():
            if v == 1:
                if s.index(k) < res:
                    res = s.index(k)
        return -1 if res == float('inf') else res


# Smarter way to implement what is on top
class Solution2:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, v in enumerate(s):
            if v in d:
                # Replace repeated terms with infinity
                d[v] = float('inf')
            else:
                d[v] = i
        res = min(d.values())
        return res if res != float('inf') else -1


# Use counter
class Solution3:
    def firstUniqChar(self, s: str) -> int:
        c, res = Counter(s), float('inf')
        for k in c:
            if c[k] == 1:
                if s.index(k) < res:
                    res = s.index(k)
        return -1 if res == float('inf') else res


# Technically can just return
class Solution4:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        for i, v in enumerate(s):
            if c[v] == 1:
                return i
        return -1

