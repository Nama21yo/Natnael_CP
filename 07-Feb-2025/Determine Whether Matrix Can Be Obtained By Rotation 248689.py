# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        if mat == target:
            return True

        deg = 3 # 90, 180, 270

        while deg:
            # Transpose the matrxi
            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j],mat[j][i] = mat[j][i],mat[i][j]
            # Reverse it
            for i in range(n):
                mat[i] = mat[i][::-1]
            
            if mat == target:
                return True
            
            deg -= 1
        

        return False