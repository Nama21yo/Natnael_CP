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
    # Kadane's Algorithm
    # Let's go the past when it becomes burden
    pre_sum = 0
    max_sum = float("-inf")

    for num in nums:
        pre_sum += num
        max_sum = max(max_sum, pre_sum)

        if pre_sum < 0:
            pre_sum = 0
    return max_sum

def main():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    print(solve(nums,n))

if __name__ == "__main__":
    main()
