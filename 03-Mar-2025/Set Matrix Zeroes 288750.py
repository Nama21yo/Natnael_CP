# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(selfp, mat: List[List[int]]) -> None:
        map_rows = set() # for duplicates
        map_cols = set()

        n = len(mat)
        m = len(mat[0])

        for r in range(n):
            for c in range(m):
                if mat[r][c] == 0:
                    map_rows.add(r)
                    map_cols.add(c)
        # update the mat
        for r in map_rows:
            for c in range(m):
                mat[r][c] = 0
        for c in map_cols:
            for r in range(n):
                mat[r][c] = 0
