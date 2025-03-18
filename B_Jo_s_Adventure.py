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

def solve(prefix_d,l,r, suffix_d):
    # print(suffix_d/)
    if l > r:
        return suffix_d[l - 1] - suffix_d[r - 1]
    return prefix_d[r - 1] - prefix_d[l - 1]

def main():
    # n = iinp()
    n,q = linp()
    nums = linp()

    prefix_d = [0]*(n)
    for i in range(1,n):
        if nums[i - 1] > nums[i]:
            prefix_d[i] = nums[i - 1] - nums[i]
        else:
            prefix_d[i] = 0
    # print(prefix_d)
    for i in range(1, n):
        prefix_d[i] = prefix_d[i - 1] + prefix_d[i]

    suffix_d = [0]*n
    for i in range(n - 2,-1, -1):
        if nums[i + 1] > nums[i]:
            suffix_d[i + 1] = nums[i + 1] - nums[i]
        else:
            suffix_d[i] = 0
    for i in range(1, n):
        suffix_d[i] = suffix_d[i - 1] + suffix_d[i]
    for _ in range(q):
        l,r = linp()
        print(solve(prefix_d,l,r, suffix_d))

if __name__ == '__main__':
    main()