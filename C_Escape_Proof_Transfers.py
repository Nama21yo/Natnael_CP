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

def solve(n,t,c,pr):
    count = 0
    l = 0
    r = 0
    while r < n:
        if l < n and pr[r] > t:
            l = r + 1
        if l < n and r - l + 1 >= c:
            count += 1
        r += 1
    return count


def main():
    # n = iinp()
    n, t, c = linp()
    pr = linp()
    print(solve(n,t,c,pr))

if __name__ == '__main__':
    main()