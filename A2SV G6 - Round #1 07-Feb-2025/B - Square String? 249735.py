# Problem: B - Square String? - https://codeforces.com/gym/585107/problem/B

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
    if len(s) == 1:
        return "NO"
    half = len(s) // 2 if len(s) % 2 == 0 else len(s) // 2 + 1
    return "YES" if s[:half] == s[half:] else "NO"

def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        print(solve(s))

if __name__ == "__main__":
    main()
