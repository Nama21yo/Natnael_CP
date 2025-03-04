# Problem: A - Kibr and His Musics - https://codeforces.com/gym/589822/problem/A

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
    n, m = map(int, input().split())
    
    prefix = []
    for i in range(n):
        c, t = map(int, input().split())
        prefix.append(c * t)
        if i > 0:
            prefix[i] += prefix[i - 1]
    
    moments = list(map(int, input().split()))
    
    i = 0
    result = []
    for j in range(m):
        while prefix[i] < moments[j]:
            i += 1
        result.append(i + 1)
    
    return result

def main():
    print(*solve(), sep="\n")

if __name__ == '__main__':
    main()
