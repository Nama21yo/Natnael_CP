# Problem: A - Nth Digit in Sequence - https://codeforces.com/gym/588468/problem/A

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

def solve(n):
    nums = list(map(str,range(1,1000)))
    numbers = "".join(nums)
    return numbers[n - 1]

def main():
    n = int(input().strip())
    print(solve(n))

if __name__ == "__main__":
    main()
