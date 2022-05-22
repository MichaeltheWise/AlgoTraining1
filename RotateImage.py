# -*- coding: utf-8 -*-
"""
Created on Sat May 21 2022

@author: Michael Lin
"""
from typing import List


class Solution1:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Observe the transformation: first zip, flip, then write back
        j = 0
        for i in zip(*matrix):
            matrix[j] = (list(i)[::-1])
            j += 1


# Same idea but perhaps fulfill the requirement much better
# This time, swap by diagonal then flip
class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i + 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]


# Direct swap
class Solution3:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2 + n%2):
            for j in range(n//2):
                temp = matrix[i][j]
                matrix[i][j] = matrix[abs(j-(n-1))][i]
                matrix[abs(j-(n-1))][i] = matrix[abs(i-(n-1))][abs(j-(n-1))]
                matrix[abs(i-(n-1))][abs(j-(n-1))] = matrix[j][abs(i-(n-1))]
                matrix[j][abs(i-(n-1))] = temp
