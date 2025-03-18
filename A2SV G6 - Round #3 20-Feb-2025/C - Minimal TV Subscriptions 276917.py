# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

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

def solve(nums, n, k , d):
   window =  d
   l = 0
   distinct = 0
   count_d = defaultdict(int)

   min_sub = float("inf")
   for r in range(n):
        count_d[nums[r]] += 1
        if r - l + 1 > window:
            count_d[nums[l]] -= 1
            if count_d[nums[l]] == 0:
                count_d.pop(nums[l])
            l += 1
        if r - l + 1 == window:
            min_sub = min(min_sub, len(count_d))
   return min_sub


def main():
    # s = input().strip()
    t = int(input().strip())
    for _ in range(t):
        n , k, d = list(map(int, input().split()))
        nums = list(map(int, input().split()))
        print(solve(nums, n, k , d))

if __name__ == "__main__":
    main()
