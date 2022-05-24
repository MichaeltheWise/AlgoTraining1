# -*- coding: utf-8 -*-
"""
Created on Sun May 22 2022

@author: Michael Lin
"""
from typing import List


class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in zip(*strs):
            if len(set(i)) == 1:
                res += i[0]
            else:
                break
        return res


# Double loop implementation
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        min_len = len(strs[0])

        if not strs:
            return res

        for i in range(1, len(strs)):
            min_len = min(min_len, len(strs[i]))

        for i in range(min_len):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return res
            res += char

        return res


# Simpler implementation
class Solution3:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        if not strs:
            return res

        min_str = min(strs)
        max_str = max(strs)
        for i, c in enumerate(min_str):
            if c != max_str[i]:
                return min_str[:i]
        return min_str
