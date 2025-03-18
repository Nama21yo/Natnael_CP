from __future__ import division, print_function
import itertools
import sys
import os
from collections import defaultdict
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

def solve(n):
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[-1]]

    mat = [[0] * n for _ in range(n)]
    # first write the odd digit then the even one
    # inorder not to be adjacent

    odd = 1
    even = 2
    total = n * n

    # Fill odd numbers first
    for i in range(n):
        for j in range(n):
            if odd <= total:
                mat[i][j] = odd
                odd += 2

    # Fill even numbers next
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 0:
                mat[i][j] = even
                even += 2
    return mat
def main():
    tests = int(input())
    sizes = [int(input()) for _ in range(tests)]

    for n in sizes:
        result = solve(n)
        for row in result:
            print(" ".join(map(str, row)))
if __name__ == "__main__":
    main()
