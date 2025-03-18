# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

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

# def solve():
#     return 'dsvgfbh'  # Implement solution here

def main():
    n = iinp()
    nums = linp()
    n = len(nums)
    nums.sort()
    median = nums[n // 2] if n % 2 else nums[(n // 2) - 1]
    print(median)
    # print(solve())

if __name__ == '__main__':
    main()