# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

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

def solve(nums, n):
    count_pair = defaultdict(int)
    ans = 0
    for i in range(n):
        nums[i] = nums[i] - i
        ans += count_pair[nums[i]]
        count_pair[nums[i]] += 1

    return ans


def main():
    t = int(input().strip())
    for _ in range(t):
        n =  int(input().strip())
        nums = list(map(int, input().split()))
        print(solve(nums, n))

if __name__ == "__main__":
    main()
