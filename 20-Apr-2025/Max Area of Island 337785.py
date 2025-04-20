# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        def inbound(row, col):
            return 0 <= row < rows and 0 <= col < cols
        def dfs(row, col):
            if not inbound(row, col) or grid[row][col] == 0 or visited[row][col]:
                return 0

            visited[row][col] = True
            area = 1  # count the current cell
            for dr, dc in directions:
                area += dfs(row + dr, col + dc)
            return area
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area
