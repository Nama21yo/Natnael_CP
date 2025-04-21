# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        rows, cols = len(grid) , len(grid[0])
        distance = [[float("inf") for j in range(cols)] for i in range(rows)]
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
                    distance[r][c] = 0
        directions = [(0,1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return (0 <= row < rows and 0 <= col < cols)
        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                new_row , new_col = row + dr, col + dc
                if inbound(new_row, new_col) and distance[new_row][new_col] == float("inf") and grid[new_row][new_col] != 0:
                    if grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        fresh -= 1
                    distance[new_row][new_col] = distance[row][col] + 1
                    queue.append((new_row, new_col))
        min_days = 0
        for r in range(rows):
            for c in range(cols):
                if distance[r][c] != float("inf"):
                    min_days = max(min_days, distance[r][c])
        return min_days if fresh == 0 else -1

            
