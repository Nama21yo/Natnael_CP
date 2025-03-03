# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = m - 1
        # choose 7 b/c left is dec and dow is inc
        # stair case search
        while i < n and j >= 0:
            if matrix[i][j] < target: # increasing
                i += 1 # go down
            elif matrix[i][j] > target: # decreasing
                j -= 1 # go left 
            else:
                return True
        return False