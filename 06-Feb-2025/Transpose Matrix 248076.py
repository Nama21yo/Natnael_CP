# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])

        transpose_matrix = [[0]*n for _ in range(m)]

        for row in range(n):
            for col in range(m):
                # if it where square matrix swap only the upper triangular matrix
                transpose_matrix[col][row] = matrix[row][col]
        return transpose_matrix