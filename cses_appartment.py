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

def solve(applicant,appartment,n,m,k):
    applicant.sort()
    appartment.sort()
    distribute = 0
    l = 0
    r = 0
    while l < n:
        while r < m and  applicant[l] - k > appartment[r]:
            r += 1
        if r < m and abs(appartment[r] - applicant[l]) <= k:
            # The problem can be solved greedily because once an apartment is allocated to an applicant, it cannot be reassigned.
            distribute += 1
            l += 1
            r += 1
        else:
            # need to move the applicant
            l += 1
    return distribute

def main():
    n,m,k = list(map(int, input().split()))
    applicant = list(map(int, input().split()))
    appartment = list(map(int, input().split()))
    print(solve(applicant,appartment,n,m,k))

if __name__ == "__main__":
    main()
