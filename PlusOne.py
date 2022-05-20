# -*- coding: utf-8 -*-
"""
Created on Thu May 19 2022

@author: Michael Lin
"""
from typing import List


class Solution1:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Switch it backwards and just add until the end
        digits, i = digits[::-1], 0
        while i < len(digits):
            if digits[i] < 9:
                digits[i] += 1
                return digits[::-1]
            else:
                digits[i] = 0
            i += 1
        digits.append(1)
        return digits[::-1]  # Flip it around at the end


# Pythonic implementation
class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        d = str()
        for _ in digits:
            d += str(_)
        d = int(d)
        d += 1
        return list(str(d))


# Separate implementation
class Solution3:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Simple case
        if 0 <= digits[-1] <= 8:
            digits[-1] += 1
            return digits

        # Complicated case
        carry = True
        index = -1
        while carry:
            if abs(index) > len(digits):
                # Add an extra 1
                digits.insert(0, 1)
                return digits
            if digits[index] == 9:
                digits[index] = 0
            else:
                digits[index] += 1
                carry = False
            index -= 1
        return digits