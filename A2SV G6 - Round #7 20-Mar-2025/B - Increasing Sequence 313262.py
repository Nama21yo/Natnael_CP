# Problem: B - Increasing Sequence - https://codeforces.com/gym/596141/problem/B

import itertools
from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil, sqrt

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def iinp():
    return int(input().strip())

def linp():
    return list(map(int, input().strip().split()))

def string():
    return input().strip()

def lsinp():
    return input().strip().split()

def digit():
    return [int(i) for i in input().strip()]

def character():
    return list(input().strip())

def solve():
    n = iinp()
    a = linp()

    curr = 0
    b = []
    for i in range(n):
        if a[i] != curr + 1:
            b.append(curr + 1)
        else:
            b.append(a[i] + 1)
        curr = b[-1]
    return b[n - 1]
def main():
    t = iinp()
    # nums = linp()
    for _ in range(t):
        print(solve())

if __name__ == '__main__':
    main()
