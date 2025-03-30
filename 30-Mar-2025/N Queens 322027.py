# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diagonal = set() # / r + c is the same
        neg_diagonal = set() # \ r - c is the same

        board = [["."] * n for _ in range(n)]
        valid_board = []
        def backtrack(r):
            if r == n:
                valid_board.append(["".join(r) for r in board])
                return
            
            for c in range(n):
                if c in cols or (r + c) in pos_diagonal or (r - c) in neg_diagonal:
                    continue
                cols.add(c)
                pos_diagonal.add(r + c)
                neg_diagonal.add(r - c)
                board[r][c] = "Q"
                
                backtrack(r + 1)

                cols.remove(c)
                pos_diagonal.remove(r + c)
                neg_diagonal.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return valid_board

            
