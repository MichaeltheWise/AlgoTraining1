# -*- coding: utf-8 -*-
"""
Created on Sun May 22 2022

@author: Michael Lin
"""


# Didn't account for floating point numbers
class Solution1:
    def myAtoi(self, s: str) -> int:
        # Step 1: Remove leading white space
        s = s.strip()

        # Step 2: Check leading character
        if s[0] == '-':
            neg_flag = 1
            s = s[1:]
        elif s[0].isdigit():
            neg_flag = 0
        else:
            return 0

        # Step 3: Read in
        res, j = 0, 0
        s = s[::-1]
        for i in range(len(s)):
            if s[i].isdigit():
                res += int(s[i]) * (10 ** j)
                j += 1

        res = -res if neg_flag else res
        if res > 2 ** 31 - 1:
            return 2 ** 31 - 1

        if res < -2 ** 31:
            return -2 ** 31

        return res


class Solution2:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        n, i, res, flag = len(s), 0, 0, '+'

        while i < n and s[i] == " ":
            i += 1  # ignoring whitespace

        if i < len(s) and (s[i] == "-" or s[i] == "+"):
            flag = s[i]
            i += 1

        while i < len(s):
            if s[i].isdigit():
                res = res * 10 + int(s[i])
                i += 1
            else:
                break

        res = res if flag == "+" else -res
        res = min(res, 2 ** 31 - 1)
        res = max(-(2 ** 31), res)

        return res