# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

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

def solve(s):
    default = "codeforces"
    count = 0
    for i,char in enumerate(s):
        if default[i] != char:
            count += 1
    return count


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        print(solve(s))

if __name__ == "__main__":
    main()
