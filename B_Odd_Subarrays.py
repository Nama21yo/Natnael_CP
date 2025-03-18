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
    n = iinp()
    nums = linp()
    subarray = 0
    i = 1
    while i < n:
        if nums[i - 1] > nums[i]:
            subarray += 1
            i += 2
        else:
            i += 1
    return subarray

def main():
    t = iinp()
    for  _ in range(t):
        print(solve())

if __name__ == '__main__':
    main()