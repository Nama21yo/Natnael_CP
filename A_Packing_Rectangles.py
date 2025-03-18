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

def can_fit(mid, a,b,n):
    return ceil(mid//a) * ceil(mid//b) >= n
def solve(w,h,n):
    l = 0
    r = max(w,h) * n

    while r - l > 1:
        mid = l + (r - l)//2
        if can_fit(mid,w,h,n):
            r = mid
        else:
            l = mid
    return r
def main():
    # n = iinp()
    w,h,n = linp()
    print(solve(w,h,n))

if __name__ == '__main__':
    main()