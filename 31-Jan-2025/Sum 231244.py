# Problem: Sum - https://codeforces.com/contest/1742/problem/A

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

def solve(a, b, c):
    if a + b == c or a + c == b or b + c == a:
        return "YES"
    return "NO"

def main():
    t = int(input().strip())
    for _ in range(t):
        a, b, c = map(int, input().split())
        print(solve(a, b, c))

if __name__ == "__main__":
    main()
