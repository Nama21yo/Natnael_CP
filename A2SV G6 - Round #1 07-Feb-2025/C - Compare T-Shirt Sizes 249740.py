# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

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

def solve(n, m):
    if n == m:
        return "="

    if n == "M":
        return "<" if m != "M" and "L" in m else ">"
    if m == "M":
        return ">" if n != "M" and "L" in n else "<"

    count_n = n.count("X")
    count_m = m.count("X")

    if "S" in n and "S" in m:
        return "<" if count_n > count_m else ">" if count_n < count_m else "="
    if "S" in n:
        return "<"
    if "S" in m:
        return ">"

    if "L" in n and "L" in m:
        return ">" if count_n > count_m else "<" if count_n < count_m else "="
    if "L" in n:
        return ">"
    if "L" in m:
        return "<"

    return "="

def main():
    t = int(input().strip())
    for _ in range(t):
        n, m = input().split()
        print(solve(n, m))

if __name__ == "__main__":
    main()

