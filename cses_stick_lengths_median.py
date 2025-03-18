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
    # first you should sort it
    nums.sort()
    # the median is the best choice
    median = nums[n // 2]
    ans = 0
    for length in nums:
        ans += abs(median - length)
    return ans

def main():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    print(solve(nums,n))

if __name__ == "__main__":
    main()
