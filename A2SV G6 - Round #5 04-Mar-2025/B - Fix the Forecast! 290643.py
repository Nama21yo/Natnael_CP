# Problem: B - Fix the Forecast! - https://codeforces.com/gym/591928/problem/B

from functools import cmp_to_key
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
    n, k = map(int, input().split())
    a = []
    for i, temp in enumerate(map(int, input().split())):
        a.append((temp, i))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = [0] * n
    for i in range(n):
        ans[a[i][1]] = b[i]
    
    print(*ans)
def main():
    t = iinp()
    for _ in range(t):
        solve()

if __name__ == '__main__':
    main()
