# Problem: Set Matrix Zeroes - https://leetcode.com/problems/set-matrix-zeroes/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        col0 = 1
        # First pass: Mark the rows and columns that need to be set to zero
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        
        # Second pass: Use the marks to set elements to zero
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != 0:
                    if matrix[0][j] == 0 or matrix[i][0] == 0:  # Corrected condition
                        matrix[i][j] = 0
        
        # If the first row needs to be set to zero
        if matrix[0][0] == 0: 
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        
        # If the first column needs to be set to zero
        if col0 == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0
