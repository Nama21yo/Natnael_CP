# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m = len(image)  # Number of rows
        n = len(image[0])  # Number of columns
        orgColor = image[sr][sc]  # Original color of the starting pixel
        
        # If the target color is the same as the original, no changes are needed
        if orgColor == color:
            return image
        
        def dfs(row, col):
            # Base case: out of bounds or pixel color is not the original color
            if (row < 0 or row >= m or col < 0 or col >= n 
                or image[row][col] != orgColor):
                return 
            
            image[row][col] = color  # Update pixel color
            
            # Recursively visit neighbors (up, down, left, right)
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        dfs(sr, sc)  # Start DFS from the given pixel
        return image
