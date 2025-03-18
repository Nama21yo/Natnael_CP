# Problem: A - Make the Product Zero - https://codeforces.com/gym/586960/problem/A

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

def solve(nums, n):
    for i, num in enumerate(nums):
        nums[i] = abs(num)
    mini = float("inf")
    for num in nums:
        mini = min(num, mini)
    return mini

def main():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    print(solve(nums, n))

if __name__ == "__main__":
    main()
