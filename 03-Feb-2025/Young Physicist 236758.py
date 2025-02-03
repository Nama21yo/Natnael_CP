# Problem: Young Physicist - https://codeforces.com/problemset/problem/69/A

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

def solve():
    n = int(input())
    sum_x = sum_y = sum_z = 0
    for _ in range(n):
        x, y, z = map(int, input().split())
        sum_x += x
        sum_y += y
        sum_z += z

    if sum_x == 0 and sum_y == 0 and sum_z == 0:
        print("YES")
    else:
        print("NO")

def main():
    solve()

if __name__ == "__main__":
    main()
