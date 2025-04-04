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
def can_be_cut(ropes,mid,k,n):
    return sum([rope//mid for rope in ropes]) >= k
def solve(ropes,n,k):
    l = 0
    r = 1e8
    for i in range(100):
        mid = l + (r - l)/2 # remember it is double not int
        if can_be_cut(ropes,mid, k,n):
            l = mid
        else:
            r = mid
    return l
def main():
    n, k = linp()
    ropes = [int(input()) for _ in range(n)] 
    print(solve(ropes,n,k))

if __name__ == '__main__':
    main()