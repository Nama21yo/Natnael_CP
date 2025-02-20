# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D

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

def check_mine(val,i,j,n,m,mat):
    sum_bomb = 0
    for r in range(i - 1, i + 2):
        for c in range(j - 1, j + 2):
            if r >= 0 and r < n and c >= 0 and c < m and mat[r][c] == "*":
                sum_bomb += 1
    return sum_bomb
def solve(mat, n , m):
    for i in range(n):
        for j in range(m):
            if mat[i][j].isdigit():
                adjacent_bomb = check_mine(mat[i][j],i,j,n,m,mat)
                if adjacent_bomb != int(mat[i][j]):
                    return "NO"
            elif mat[i][j] == ".":
                adjacent_bomb = check_mine(mat[i][j],i,j,n,m,mat)
                if adjacent_bomb != 0:
                    return "NO"

    return "YES"


def main():
    # t = int(input().strip())
    mat = []
    n,m = list(map(int, input().split()))
    for _ in range(n):
        row = list(input())
        mat.append(row)
    print(solve(mat, n, m))

if __name__ == "__main__":
    main()
