# Problem: D - Repeating Cipher - https://codeforces.com/gym/585107/problem/D

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

def solve(s, t):
    decrypted = ""
    i = 0
    j = 0
    while i < t:
        decrypted += s[i]
        j += 1
        i = i + j
    return decrypted


def main():
    t = int(input().strip())
    s = input().strip()
    # num_list = list(map(int, input().split()))
    print(solve(s, t))

if __name__ == "__main__":
    main()
