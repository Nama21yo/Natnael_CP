# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

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

def solve(nums, n , total):
    nums.sort()
    fronts = nums[:n]
    backs = nums[n:]
    count = 0
    for back,front in zip(backs,fronts):
        if back - front >= total:
            count += 1
    return "YES" if count >= n else "NO"

def main():
    # s = input().strip()
    t = int(input().strip())
    for _ in range(t):
        n , total = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        print(solve(nums, n, total))

if __name__ == "__main__":
    main()
