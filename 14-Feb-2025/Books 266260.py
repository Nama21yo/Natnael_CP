# Problem: Books - https://codeforces.com/contest/279/problem/B

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

def solve(nums,n,t):
    l = 0
    current_time = 0
    max_book = 0
    for r in range(n):
        current_time += nums[r]

        while l <= r and current_time > t:
            current_time -= nums[l]
            l += 1

        max_book = max(max_book , r - l + 1)
    return max_book


def main():
    n,t = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    print(solve(nums,n,t))

if __name__ == "__main__":
    main()
