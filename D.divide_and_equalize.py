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

def solve(nums, n):
    count_pair = defaultdict(int)
    ans = 0
    for i in range(n):
        nums[i] = nums[i] - i
        ans += ans[nums[i]]
        ans[nums[i]] += 1

    return ans


def main():
    t = int(input().strip())
    for _ in range(t):
        n =  int(input().strip())
        nums = list(map(int, input().split()))
        print(solve(nums, n))

if __name__ == "__main__":
    main()
