# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/


# import math

# def nCr(n, r): # 1 - based index
#     res = 1

#     # calculating nCr:
#     for i in range(r): 
#         res = res * (n - i)
#         res = res // (i + 1)

#     return res

# def pascalTriangle(r, c):
#     element = nCr(r - 1, c - 1)
#     return element

# if __name__ == '__main__':
#     r = 5 # row number
#     c = 3 # col number
#     element = pascalTriangle(r, c)
#     print(f"The element at position (r,c) is: {element}")
    
        
        
class Solution:
    def comb(self,n, r):
        res = 1
        for i in range(r):
            res *= (n - i)
            res //= (i + 1)
        return res
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i in range(rowIndex + 1):
            ans.append(self.comb(rowIndex, i))
        return ans
        