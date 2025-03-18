# Problem: Divide and equalize - https://codeforces.com/problemset/problem/1881/D

from __future__ import division, print_function
import itertools
import sys
import os
from collections import defaultdict

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
def prime_factors(n):
    i = 2
    factors = defaultdict(int)
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i] += 1
    if n > 1:
        factors[n] += 1
    return factors
def divide_and_equalize(nums, n):
    factor_counts = defaultdict(int)

    for num in nums:
        factors = prime_factors(num)
        for factor, count in factors.items():
            factor_counts[factor] += count

    for key, value in factor_counts.items():
        # if it I can't balance the primes
        if factor_counts[key] % n != 0:
            return False
    return True


def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        num_list = list(map(int, input().split()))
        print("YES" if divide_and_equalize(num_list, n) else "NO")

if __name__ == "__main__":
    main()
