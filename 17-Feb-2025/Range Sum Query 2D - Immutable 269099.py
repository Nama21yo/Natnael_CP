# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix_sum = []
            return
        
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * cols for _ in range(rows)]
        
        # Fill first cell
        self.prefix_sum[0][0] = matrix[0][0]

        # Fill first row
        for j in range(1, cols):
            self.prefix_sum[0][j] = self.prefix_sum[0][j - 1] + matrix[0][j]

        # Fill first column
        for i in range(1, rows):
            self.prefix_sum[i][0] = self.prefix_sum[i - 1][0] + matrix[i][0]
        
        # Build the prefix sum matrix
        for i in range(1, rows):
            for j in range(1, cols):
                self.prefix_sum[i][j] = (self.prefix_sum[i - 1][j] + self.prefix_sum[i][j - 1] -
                    self.prefix_sum[i - 1][j - 1] + matrix[i][j])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # exchange row1 >> row2 when constant(no decrement or increment)
        # exchange col1 >> col2 when constant (no decrement or increment)
        if row1 == 0 and col1 == 0:
            return self.prefix_sum[row2][col2]
        
        if row1 == 0:
            return self.prefix_sum[row2][col2] - self.prefix_sum[row2][col1 - 1]
        
        if col1 == 0:
            return self.prefix_sum[row2][col2] - self.prefix_sum[row1 - 1][col2]
        
        return (self.prefix_sum[row2][col2] - self.prefix_sum[row1 - 1][col2] - self.prefix_sum[row2][col1 - 1] + self.prefix_sum[row1 - 1][col1 - 1])
