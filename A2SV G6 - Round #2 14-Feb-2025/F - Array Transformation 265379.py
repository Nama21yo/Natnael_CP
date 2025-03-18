# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

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

def solve(n, arr):
    freq = Counter(arr)
    counts = sorted(freq.values())
    total = sum(counts)
    min_removals = float('inf')
    prefix_sums = [0] * (len(counts) + 1)
    for i in range(1, len(counts) + 1):
        prefix_sums[i] = prefix_sums[i - 1] + counts[i - 1]
    for i, c in enumerate(counts):
        removals = prefix_sums[i] + (total - prefix_sums[i] - c * (len(counts) - i))
        min_removals = min(min_removals, removals)
    return min_removals

def main():
    t = int(input().strip())

    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().split()))
        print(solve(n, arr))

if __name__ == "__main__":
    main()
