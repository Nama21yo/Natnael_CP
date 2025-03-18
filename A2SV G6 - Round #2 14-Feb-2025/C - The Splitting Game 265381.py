# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

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

def solve(n,s):
    suffix_count = Counter(s)
    prefix_count = Counter()
    max_ans = 0

    for char in s:
        prefix_count[char] += 1
        suffix_count[char] -= 1

        if suffix_count[char] == 0:
            suffix_count.pop(char)
            # del suffix_count[char]

        max_ans = max(max_ans, len(prefix_count) + len(suffix_count))

    return max_ans

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        print(solve(n, s))


if __name__ == "__main__":
    main()
