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
# We can start from the smallest value coin and move to higher values. The main idea is to start from the coins of smallest value and build up the sum of coins we can form. Let's say we have some coins whose total value is X, so the maximum value of the next coin can be X + 1. If the next coin has a value greater than X + 1 then (X + 1) is the smallest sum which we cannot create using any subset of coins. Otherwise, if the value of the next coin is less than (X + 1) we can add it to the total value to get the new total sum X.


def solve(nums,n):
    # first you should sort it
    nums.sort()
    # find the missing sum
    missing_coin = 1
    for coin in nums:
        if coin > missing_coin:
            break
        missing_coin += coin
    return missing_coin

def main():
    n = int(input().strip())
    nums = list(map(int, input().split()))
    print(solve(nums,n))

if __name__ == "__main__":
    main()
