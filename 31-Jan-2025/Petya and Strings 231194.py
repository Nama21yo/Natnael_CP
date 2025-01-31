# Problem: Petya and Strings - https://codeforces.com/problemset/problem/112/A

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

def solve(n,m):
    n = n.lower()
    m = m.lower()
    if n < m:
        return -1
    elif  n > m:
        return 1
    else:
        return 0
    


def main():
    n = input()
    m = input()
    print(solve(n,m))

if __name__ == "__main__":
    main()
