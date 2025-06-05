# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # Get matrix dimensions
        m = len(matrix)
        n = len(matrix[0])

        # Initialize a DP table to store the longest path lengths starting from each cell
        dp = [[-1] * n for _ in range(m)]
        
        # Helper function to perform DFS with memoization
        def solve(i, j, prev):
            # Base case: If out of bounds or current value is not greater than prev, return 0
            if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] <= prev:   
                return 0
            
            # If already computed, return the cached result
            if dp[i][j] != -1:
                return dp[i][j]
    
            # Explore four possible directions (right, down, left, up)
            right = 1 + solve(i, j + 1, matrix[i][j])
            down = 1 + solve(i + 1, j, matrix[i][j])
            top = 1 + solve(i - 1, j, matrix[i][j])
            left = 1 + solve(i, j - 1, matrix[i][j])

            # Cache the result
            dp[i][j] = max(right, down, left, top)

            return dp[i][j]

        max_length = 1  # Variable to keep track of the maximum path length
        
        # Compute the longest increasing path starting from each cell
        for i in range(m):
            for j in range(n):
                max_length = max(max_length, solve(i, j, -1))
        
        return max_length



        