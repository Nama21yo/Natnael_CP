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


def solve(s):
    pass



def main():
    if not os.getenv('ONLINE_JUDGE'):
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')

    s = input().strip()
    # num = int(input().strip())
    # num_list = list(map(int, input().split()))
    print(solve(s))


if __name__ == "__main__":
    main()
