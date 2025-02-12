# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

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

def solve(nums1,nums2, n,m):
    ans = []
    l = 0
    r = 0
    k = 0
    while l < n or r < m:
        if r == m or (l < n and nums1[l] < nums2[r]):
            ans.append(nums1[l])
            l  += 1
        else:
            ans.append(nums2[r])
            r += 1
    return ans

def main():
    # s = input().strip()
    n ,m = list(map(int, input().split()))
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    print(*solve(nums1,nums2, n,m))
if __name__ == "__main__":
    main()
