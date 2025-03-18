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

def solve(c,m,q):
    n = c + m + q
    l = -1
    r = n // 3 + 1 # not fine
    while l < r - 1:
        mid = l + (r - l)//2
        if mid <= c and mid <= m and 3*mid <= n:
            l = mid
        else:
            r = mid
    return l
         


def main():
    t = iinp()
    for _ in range(t):
        c,m,q = linp()
        print(solve(c,m,q))

if __name__ == '__main__':
    main()