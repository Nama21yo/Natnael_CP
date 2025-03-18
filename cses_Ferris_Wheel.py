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

def solve(children,n,x):
    children.sort()
    l = 0
    r = n - 1
    gondolas = 0
    # same as boats to save people
    while l <= r:
        if children[l] + children[r] > x:
            gondolas += 1
            r -= 1
        elif children[l] + children[r] <= x:
            gondolas += 1
            l += 1
            r -= 1
    return gondolas

def main():
    n,x= list(map(int, input().split()))
    children = list(map(int, input().split()))
    print(solve(children,n,x))

if __name__ == "__main__":
    main()
