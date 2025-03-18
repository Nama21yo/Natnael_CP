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
def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes

def count_almost_primes(n):
    primes = sieve_of_eratosthenes(n)
    almost_prime_count = 0
    for i in range(2, n + 1):
        num = i
        divisors_count = 0

        for prime in primes:
            if prime * prime > num:
                break
            if num % prime == 0:
                divisors_count += 1
                while num % prime == 0:
                    num //= prime
        if num > 1:
            divisors_count += 1
        if divisors_count == 2:
            almost_prime_count += 1
    return almost_prime_count

if __name__ == "__main__":
    n = int(input().strip())
    print(count_almost_primes(n))
