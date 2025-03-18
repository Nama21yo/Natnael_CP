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

def solve(coin, nums,n):
    nums.sort()
    # bisect left
    l = -1
    r = n 
    while l < r - 1:
        mid = l + (r - l)//2
        if nums[mid] <= coin:
            l = mid
        else:
            r = mid
    return l + 1


def main():
    n = iinp()
    nums = linp()
    t = iinp()
    for _ in range(t):
        coin = iinp()
        print(solve(coin, nums,n))

if __name__ == '__main__':
    main()