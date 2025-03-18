# Problem: Remove Smallest - https://codeforces.com/problemset/problem/1399/A

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

def solve(nums,n):
    # greedy + sorting
    nums.sort()
    for i in range(n - 1):
        if nums[i + 1]  - nums[i] > 1:
            return "NO"
    return "YES"

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        nums = list(map(int, input().split()))
        print(solve(nums,n))

if __name__ == "__main__":
    main()
