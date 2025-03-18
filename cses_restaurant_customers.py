from __future__ import division, print_function
import itertools
import sys
import os
import bisect
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

def solve(events):
    start = sorted([event[0] for event in events])
    end = sorted([event[1] for event in events])
    n = len(start)
    m = len(end)

    i = 0
    j = 0
    max_customer = 0
    current_customer = 0
    # use two pointers like merge sort
    while i < n and j < m:
        # Customer arrives before or exactly at the departure of
        # the previous customer
        if start[i] <= end[j]:
            current_customer += 1
            i += 1
        else:
            current_customer -= 1
            j += 1
        max_customer = max(max_customer,current_customer)
    return max_customer


def main():
    events = []
    n = int(input())
    for _ in range(n):
        event = list(map(int, input().split()))
        events.append(event)
    print(solve(events))

if __name__ == "__main__":
    main()
