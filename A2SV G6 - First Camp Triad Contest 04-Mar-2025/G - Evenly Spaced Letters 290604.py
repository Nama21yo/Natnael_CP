# Problem: G - Evenly Spaced Letters - https://codeforces.com/gym/589822/problem/G

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

def solve(s):
    return "".join(sorted(s))

def main():
    t = iinp()
    for _ in range(t):
        s = string()
        print(solve(s))

if __name__ == '__main__':
    main()