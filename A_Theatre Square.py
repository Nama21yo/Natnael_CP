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

def theatre(n,m,a):
    p1 = (n + a - 1 ) // a # ceil(n / a )
    p2 = (m + a - 1) // a # ceil(m / a)
    return p1 * p2


def main():
    n, m, a = list(map(int, input().split()))
    print(theatre(n,m,a))

if __name__ == "__main__":
    main()
