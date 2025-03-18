# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

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
    n , k = linp()
    nums = linp()
    difference = []
    for i in range(1, n):
        difference.append(nums[i - 1] - nums[i]) #put it as neagtive
    difference.sort()
    ans = nums[n - 1] - nums[0]
    for i in range(k - 1):
        ans += difference[i]
    return ans

def main():
    print(solve())

if __name__ == '__main__':
    main()