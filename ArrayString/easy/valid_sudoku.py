from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()

        # Row wise checking

        def verify(l):
            l = [i for i in l if i != "."]
            return len(l) == len(set(l))

        for row in board:
            if not verify(row):
                return False

        # Col wise checking
        for col in zip(*board):
            if not verify(col):
                return False

        # Grid wise checking
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                l = board[i][j:j + 3] + board[i + 1][j:j + 3] + board[i + 2][j:j + 3]
                if not verify(l):
                    return False
        return True

