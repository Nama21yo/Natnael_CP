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

def solve(r,b,n,m):
    for i in range(1,n):
        r[i] = r[i - 1] + r[i]
    for i in range(1, m):
        b[i] = b[i - 1] + b[i]
    
    return max(0, max(r)) + max(0, max(b))
def main():
    t = iinp()
    for _ in range(t):
        n = iinp()
        r = linp()
        m = iinp()
        b = linp()
        print(solve(r,b,n,m))

if __name__ == '__main__':
    main()