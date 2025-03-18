# Problem: F - Covered Points Count - https://codeforces.com/gym/589822/problem/F

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
    events = defaultdict(int)

    for _ in range(n):
        l, r = linp()
        events[l] += 1
        events[r + 1] -= 1

    keys = sorted(events.keys())
    coverage = 0
    prev = keys[0]
    result = defaultdict(int)
    for point in keys:
        result[coverage] += point - prev
        coverage += events[point]
        prev = point

    ans = [result[k] for k in range(1, n + 1)]
    print(*ans)
def main():
    solve()

if __name__ == '__main__':
    main()