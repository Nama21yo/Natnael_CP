# Problem: A - Vus the Cossack and a Contest - https://codeforces.com/gym/585107/problem/A

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

def solve(nums):
    n = nums[0]
    m = nums[1]
    k = nums[2]
    if m < n or k < n:
        return "NO"
    return "YES"


def main():
    nums = list(map(int, input().split()))
    print(solve(nums))

if __name__ == "__main__":
    main()
