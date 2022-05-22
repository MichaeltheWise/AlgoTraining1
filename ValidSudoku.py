# -*- coding: utf-8 -*-
"""
Created on Sat May 21 2022

@author: Michael Lin
"""
from typing import List
from collections import defaultdict


class Solution1:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Vertical validation
        for i in zip(*board):
            if not self.check(i):
                return False

        # Horizontal validation
        for i in board:
            if not self.check(i):
                return False

        # Square validation
        final_list = []
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                temp_list = [board[i][j], board[i + 1][j], board[i + 2][j],
                             board[i][j + 1], board[i + 1][j + 1], board[i + 2][j + 1],
                             board[i][j + 2], board[i + 1][j + 2], board[i + 2][j + 2]]
                final_list.append(temp_list)

        for i in final_list:
            if not self.check(i):
                return False

        return True

    def check(self, l: List[str]):
        num_l = [v for v in l if v != '.']
        if len(num_l) != len(set(num_l)):
            return False
        return True


# Smart clean way of doing it using floor but slower
class Solution2:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n == '.':
                    continue

                box_index = (i // 3, j // 3)

                # If numbers already exist, then return false
                if n in rows[i] or n in cols[j] or n in boxes[box_index]:
                    return False

                # If doesn't exist, add
                rows[i].add(n)
                cols[j].add(n)
                boxes[box_index].add(n)
        return True

