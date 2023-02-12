from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m, n = len(grid), len(grid[0])
        self.area = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 1:
                    self.dfs(i, j, m, n, grid)
                    max_area = max(max_area, self.area)
                    self.area = 0

        return max_area

    # Bring in the non-local variable area and update it everytime we move to the correct dfs location ONLY
    def dfs(self, i, j, m, n, grid):
        if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
            self.area += 1
            grid[i][j] = 0
        else:
            return

        for nr, nc in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            self.dfs(i, j, m, n, grid)