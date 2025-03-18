# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

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

def solve(mat):
    n = len(mat)
    m = len(mat[0])
    good_sum = 0
    # the midd one
    for i in range(n):
        for j in range(m):
            if  i == (n - 1)// 2 or j == ((m - 1) // 2):
                good_sum += mat[i][j]
    # only the diagonal
    for i in range(n - 1, -1, -1):
        good_sum += mat[i][n - i - 1]
    # the second diagonal
    for i in range(n):
        for j in range(m):
            if  i == j:
                # print(i,j)
                good_sum += mat[i][j]
    return good_sum - 2*mat[(n - 1)// 2][((m - 1) // 2)]



def main():
    n = int(input().strip())
    mat = []
    for _ in range(n):
        row = list(map(int, input().split()))
        mat.append(row)
    print(solve(mat))

if __name__ == "__main__":
    main()
