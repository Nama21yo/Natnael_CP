# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

from __future__ import division, print_function
import itertools
import sys
import os

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

def diagonal_Sum(diagonal,matrix,row,col, n, m):
    bishop_sum = diagonal
    # Solve for the 4 direction diagonal

    # left bottom half diagonal
    left = col - 1
    bottom = row + 1
    while left >= 0 and bottom < n:
        bishop_sum +=  matrix[bottom][left]
        left -=  1
        bottom += 1

    # left top half
    top = row - 1
    left = col - 1
    while left >= 0 and top >= 0:
        bishop_sum += matrix[top][left]
        left -= 1
        top -= 1
    # right top half
    top = row - 1
    right = col + 1
    while right < m and top >= 0:
        bishop_sum += matrix[top][right]
        right += 1
        top -= 1
    # right bottom half
    right = col + 1
    bottom = row + 1
    while bottom < n and right < m:
        bishop_sum += matrix[bottom][right]
        bottom += 1
        right += 1

    return bishop_sum




def solve(matrix, n, m):
    max_sum = 0
    # assume each element are diagonals and check
    for row in range(n):
        for col in range(m):
            current_sum = diagonal_Sum(matrix[row][col],matrix,row,col,n,m)
            max_sum = max(current_sum, max_sum)
    return max_sum



def main():
    t = int(input().strip())
    for _ in range(t):
        n,m = list(map(int, input().split()))
        matrix = []
        for _ in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)
        print(solve(matrix,n,m))

if __name__ == "__main__":
    main()
