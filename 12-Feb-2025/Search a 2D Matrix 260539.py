# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    # TC- O(log(n * m))
    # SC - O(1)
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        left = 0 
        right = (n * m) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            row = mid // m
            col = mid % m
            
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
