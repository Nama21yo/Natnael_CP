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
    nums.sort()
    count = 1
    for i in range(n - 1):
        if nums[i] != nums[i + 1]:
            count += 1
    return count
def main():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    print(solve(nums,n))

if __name__ == "__main__":
    main()
