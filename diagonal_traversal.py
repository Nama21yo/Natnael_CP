class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row, col = len(mat), len(mat[0])

        if row == 0 or col == 0:
            return []

        diagonal = [0] * (row * col)

        # control the direction of traversal
        up = True

        last = 0
        for k in range(row + col - 1):
            if up:
                i = min(k, row - 1) 
                j = k - i  
                
                while i >= 0 and j < col:
                    diagonal[last] = mat[i][j]
                    last += 1
                    i -= 1
                    j += 1
            else:
                j = min(k, col - 1)  
                i = k - j  

                while j >= 0 and i < row:
                    diagonal[last] = mat[i][j]
                    last += 1
                    i += 1
                    j -= 1
            
            up = not up  

        return diagonal
