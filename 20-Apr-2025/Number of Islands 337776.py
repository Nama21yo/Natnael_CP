# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        
        def dfs(grid, visited, row, col):
            if (not inbound(row, col)) or grid[row][col] == "0" or visited[row][col]:
                return
            visited[row][col] = True

            for dr, dc in directions:
                new_row, new_col = row + dr , col + dc
                dfs(grid, visited, new_row, new_col)
        num_island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (not visited[i][j]) and grid[i][j] == "1": # debugger
                    num_island += 1
                    dfs(grid, visited, i, j)
        return num_island
