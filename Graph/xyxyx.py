from typing import List
import sys


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        m, n = len(heights), len(heights[0])
        self.min_cost = sys.maxsize
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        current_path = set()

        def dfs(i, j, prev, max_diff_full_path):
            if (i, j) in current_path:
                return
            if i < 0 or i > m - 1 or 0 > j > n - 1:
                return
            print(i, j)
            current_diff = abs(heights[i][j] - prev)
            max_diff_full_path = max(max_diff_full_path, current_diff)
            if i == m - 1 and j == n - 1:
                self.min_cost = min(self.min_cost, max_diff_full_path)
                return

            current_path.add((i, j))
            for nr, nc in directions:
                dfs(i + nr, j + nc, heights[i][j], max_diff_full_path)
            current_path.remove((i, j))

        dfs(0, 0, heights[0][0], -sys.maxsize)

        return self.min_cost


s = Solution()
heights = [[1,2,2],[3,8,2],[5,3,5]]
s.minimumEffortPath(heights)