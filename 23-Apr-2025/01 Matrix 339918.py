# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                else:
                    mat[i][j] = float('inf')
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while queue:
            row, col, dist = queue.popleft()
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n and mat[new_row][new_col] > dist + 1:
                    mat[new_row][new_col] = dist + 1
                    queue.append((new_row, new_col, dist + 1))
        return mat