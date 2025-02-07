# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n,m  = len(img), len(img[0])

        ans = [[0]*m for _ in range(n)]

        for r in range(n):
            for c in range(m):
                # r-1 -> r + 1
                # c - 1 -> c+1
                total_sum = 0
                count = 0
                for i in range(r - 1, r + 2):
                    for j in range(c - 1 , c + 2):
                        if i < 0 or i == n or j < 0 or j == m:
                            continue
                        total_sum += img[i][j]
                        count += 1
                
                ans[r][c] = total_sum // count

        return ans 

        