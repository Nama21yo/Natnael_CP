# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows , cols = len(isWater), len(isWater[0])
        height = [[0 for _ in range(cols)] for _ in range(rows)]
        queue = deque()
        for row in range(rows):
            for col in range(cols):
                if isWater[row][col] == 1:
                    queue.append((row, col , 0))
                else:
                    height[row][col] = float("inf")
        
        # bfs
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def in_grid(r,c):
            return (0 <= r < rows) and (0 <= c < cols)
        
        while queue:
            row, col, h = queue.popleft()

            for dx, dy in directions:
                nx,ny = row + dx, col + dy
                if in_grid(nx,ny) and height[nx][ny] > h + 1:
                    height[nx][ny] = h + 1
                    queue.append((nx, ny, height[nx][ny]))
            
        return height



                    
