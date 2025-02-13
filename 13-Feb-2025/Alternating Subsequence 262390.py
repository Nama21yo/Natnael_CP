# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

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
    # either it is positive or negative
    is_Positive =  False
    max_sum = 0
    i = 0
    while i < n: 
        is_Positive = True if nums[i] > 0 else False
        maxi = nums[i]
        if is_Positive:
            while i < n and nums[i] > 0:
                maxi = max(maxi, nums[i])
                i += 1
        else:
            while i < n and nums[i] < 0:
                maxi = max(maxi, nums[i])
                i += 1
        max_sum += maxi
    return max_sum

def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        nums = list(map(int, input().split()))
        print(solve(nums,n))

if __name__ == "__main__":
    main()
