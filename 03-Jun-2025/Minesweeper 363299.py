# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        def dfs(i, j):
            count = 0
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    if 0 <= x < m and 0 <= y < n and board[x][y] == "M":
                        count += 1
            if count:
                board[i][j] = str(count)
            else:
                board[i][j] = "B"
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if 0 <= x < m and 0 <= y < n and board[x][y] == "E":
                            dfs(x, y)
        
        m, n = len(board), len(board[0])
        i , j = click
        if board[i][j] == "M":
            board[i][j] = "X"
        else:
            dfs(i, j)

        return board