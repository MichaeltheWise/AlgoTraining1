# -*- coding: utf-8 -*-
"""
Created on Sat May 14 2022

@author: Michael Lin
"""
from typing import List


class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev, i = nums[0], 1
        while i < len(nums):
            # if the same, remove
            if prev == nums[i]:
                nums.remove(nums[i])
            else:
                # if not the same, increment
                prev = nums[i]
                i += 1
        return len(nums)

# Faster but still not fast enough
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev, cur = 0, 1
        while cur < len(nums):
            if nums[prev] == nums[cur]:
                nums.pop(cur)
            else:
                prev = cur
                cur += 1
        return len(nums)

# So technically, don't need to remove element; based on question, can ignore anything after the returned index
class Solution3:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev, cur = 0, 0
        while cur < len(nums):
            if nums[prev] != nums[cur]:
                # Increment the left pointer
                prev += 1
                # Replace the duplicated value with new value
                nums[prev] = nums[cur]
            cur += 1
        return prev + 1


# Pythonic implementation
class Solution4:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        # Just use a sorted set to replace values
        s = sorted(set(nums))
        for i in range(len(s)):
            nums[i] = s[i]
        return len(s)
