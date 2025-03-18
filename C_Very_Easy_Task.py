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

def can_be_copied(mid,x,y,n):
    return (mid//x) + mid//y >= n - 1 #first copy is handled separately
def solve(n,x,y):
    if n == 1:
        return min(x,y)
    l = 0
    r = max(x ,y)*n

    while r - l > 1:
        mid = l  + (r - l)//2
        if can_be_copied(mid,x,y,n):
            r = mid
        else:
            l = mid
    return r + 1
    

def main():
    # n = iinp()
    n,x,y = linp()
    print(solve(n,x,y))

if __name__ == '__main__':
    main()