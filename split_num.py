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

def solve(s,n):
    p1 = 0
    p2 = n - 1
    while p1 < n and p2 >= 0:
        if s[p1] == s[p2]:
            break
        else:
            p2 -= 1
    if p1 == p2:
        return len(set(s[:n // 2])) + len(set(s[n//2:]))
    else:
        return len(set(s[p1: p2])) + len(set(s[p2:]))


def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        s = input().strip()
        print(solve(s, n))

if __name__ == "__main__":
    main()
