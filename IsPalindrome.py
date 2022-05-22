# -*- coding: utf-8 -*-
"""
Created on Sun May 22 2022

@author: Michael Lin
"""


class Solution1:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for i in s:
            if i.isalnum():
                res += i.lower()
        # Pythonic representation
        return res == res[::-1]


class Solution2:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for i in s:
            if i.isalnum():
                res += i.lower()

        start, end = 0, len(res) - 1
        while start < end:
            if res[start] != res[end]:
                return False
            start += 1
            end -= 1
        return True


# Pull the string processing into the while loop
class Solution3:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while start < end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            else:
                if s[start].lower() != s[end].lower():
                    return False
                start += 1
                end -= 1
        return True
