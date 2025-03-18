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


def is_subsequence(s, t):
    index_s, index_t = 0, 0
    while index_s < len(s) and index_t < len(t):
        if s[index_s] == t[index_t]:
            index_s += 1
        index_t += 1
    return index_s == len(s)

def solve(s, t, p):
    if not is_subsequence(s, t):
        return "NO"

    count_s = [0] * 26 # O(26)
    count_p = [0] * 26
    count_t = [0] * 26

    for c in s:
        count_s[ord(c) - ord('a')] += 1
    for c in p:
        count_p[ord(c) - ord('a')] += 1
    for c in t:
        count_t[ord(c) - ord('a')] += 1

    for i in range(26):
        if count_s[i] + count_p[i] < count_t[i]:
            return "NO"

    return "YES"

def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        t = input().strip()
        p = input().strip()
        print(solve(s, t, p))

if __name__ == "__main__":
    main()
