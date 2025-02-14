# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

from __future__ import division, print_function
import itertools
import sys
import os
from collections import Counter
if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def rotate(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][j]

    return rotated

def solve(mat, n):
    min_operations = 0
    rotate_90 = rotate(mat)
    rotate_180 = rotate(rotate_90)
    rotate_270 = rotate(rotate_180)

    for i in range(n // 2):
        for j in range(i, n - 1 - i):
            ans = [mat[i][j], rotate_90[i][j], rotate_180[i][j], rotate_270[i][j]]
            count_ones = ans.count('1')
            count_zeros = 4 - count_ones
            min_operations += min(count_zeros, count_ones)

    return min_operations

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        mat = []
        for _ in range(n):
            row =  list(input())
            mat.append(row)
        print(solve(mat, n))

if __name__ == "__main__":
    main()

#other method

#     min_operations = 0

#     for i in range((n + 1) // 2):
#         for j in range(n // 2):
#             vals = [
#                 mat[i][j],
#                 mat[j][n - 1 - i],
#                 mat[n - 1 - i][n - 1 - j],
#                 mat[n - 1 - j][i]
#             ]

#             ones = vals.count('1')
#             zeros = 4 - ones
#             min_operations += min(ones, zeros)

#     print(min_operations)
