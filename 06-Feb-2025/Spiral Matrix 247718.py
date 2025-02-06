# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []

        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        while left <= right and top <= bottom:
            # Traverse from left to right along the top row
            for i in range(left, right + 1):
                spiral.append(matrix[top][i])
            top += 1
            # Traverse from top to bottom along the right column
            for i in range(top, bottom + 1):
                spiral.append(matrix[i][right])
            right -= 1
            # Traverse from right to left along the bottom row
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][i])
                bottom -= 1
            # Traverse from bottom to top along the left column
            if left <= right:
                for i in range(bottom, top -1, -1):
                    spiral.append(matrix[i][left])
                left += 1
        

        return spiral