# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F


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

def solve(s,k):
    prefix_sums = defaultdict(int)
    prefix_sums[0] = 1
    count = 0
    ones_count = 0
    for char in s:
        if char == '1':
            ones_count += 1
        count += prefix_sums[ones_count - k]
        prefix_sums[ones_count] += 1
    return count

def main():
    k = int(input())
    s = input().strip()
    print(solve(s,k))

if __name__ == "__main__":
    main()
