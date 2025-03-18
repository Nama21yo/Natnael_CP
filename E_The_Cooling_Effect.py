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
    n, k  = linp()
    a = [float("inf")] * n
    index = linp()
    point = linp()
    for i in range(k):
        a[index[i] - 1] = point[i]
    b = a.copy()
    # go from left
    for l in range(1,n):
        a[l] = min(a[l], a[l - 1] + 1)
    # go from right
    for r in range(n - 2, -1, -1):
        b[r] = min(b[r], b[r + 1] + 1)
    ans = [min(ai,bi) for ai,bi in zip(a,b)]
    return ans
def main():
    t = iinp()
    for _ in range(t):
        space = linp()
        print(*solve())

if __name__ == '__main__':
    main()