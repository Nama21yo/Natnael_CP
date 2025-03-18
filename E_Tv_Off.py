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
    n = int(input())
    segments = []
    coord_set = set()
    # Collecting segments and unique coordinates
    for _ in range(n):
        l, r = map(int , input().split())
        segments.append((l, r + 1))
        coord_set.add(l)
        coord_set.add(r + 1)
    coord_list = sorted(coord_set)
    coord_map = {v: i for i, v in enumerate(coord_list)}
    m = len(coord_list)

    coverage = [0] * (m + 1)
    for l, r in segments:
        coverage[coord_map[l]] += 1
        coverage[coord_map[r]] -= 1

    for i in range(1, m):
        coverage[i] += coverage[i - 1]

    # Compute `pref` array, which stores the count of moments covered exactly once
    pref = [0] * m
    for i in range(1, m):
        pref[i] = pref[i - 1] + (1 if coverage[i - 1] == 1 else 0)
    # Find redundant segment
    for i, (l, r) in enumerate(segments):
        if pref[coord_map[r]] - pref[coord_map[l]] == 0:
            print(i + 1)
            return

    print(-1)
def main():
    # n = iinp()
    # nums = linp()
    solve()

if __name__ == '__main__':
    main()