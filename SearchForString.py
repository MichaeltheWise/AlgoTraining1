# -*- coding: utf-8 -*-
"""
Created on Sun May 22 2022

@author: Michael Lin
"""
import re


class Solution1:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        elif needle == '':
            return 0
        else:
            # Use regex search python function call
            return re.search(needle, haystack).start()


# Without function call
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        elif needle == '':
            return 0
        else:
            for i in range(len(haystack)):
                if haystack[i:i+len(needle)] == needle:
                    return i


# Most pythonic implementation
class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if needle in haystack:
            return haystack.index(needle)
        return -1
