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

def domino(n,m):
    return (n*m) // 2
# can be solve using db basically fibonnaci
# Calculate the Convex Hull?(check it out)
def main():
    # s = input().strip()
    # num = int(input().strip())
    n,m = list(map(int, input().split()))
    print(domino(n,m))

if __name__ == "__main__":
    main()
