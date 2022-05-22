# -*- coding: utf-8 -*-
"""
Created on Sun May 22 2022

@author: Michael Lin
"""
from collections import Counter


class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = []
        for v in s:
            set_s.append(v)

        for v in t:
            if v in set_s:
                set_s.remove(v)
            else:
                return False

        return False if set_s else True


# Faster implementation using dictionary
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for char in s:
            d[char] = d.get(char, 0) + 1
        for char in t:
            if char not in d:
                return False
            if d[char] == 1:
                del d[char]
            else:
                d[char] -= 1
        return len(d) == 0


# Pythonic implementation using counter
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        c_s, c_t = Counter(s), Counter(t)
        return c_s == c_t


# Can also use dictionary
class Solution4:
    def isAnagram(self, s: str, t: str) -> bool:
        d_s, d_t = {}, {}
        for v in s:
            d_s[v] = d_s.get(v, 0) + 1
        for v in t:
            d_t[v] = d_t.get(v, 0) + 1
        return d_s == d_t

