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

def solve(pre1,pre2, n, typ, l, r):
    if typ == 1:
        return pre1[r] - pre1[l - 1]
    return pre2[r] - pre2[l - 1]

def main():
    n = iinp()
    nums = linp()
    t = iinp()
    pre1 = [0]*(n + 1)
    for i in range(1, n + 1):
        pre1[i] = pre1[i - 1] + nums[i - 1]
    sort_nums  = sorted(nums)
    pre2 = [0]*(n + 1)
    for i in range(1, n + 1):
        pre2[i] = pre2[i - 1] + sort_nums[i - 1]
    for _ in range(t):
        typ, l, r = linp()
        print(solve(pre1, pre2,n, typ, l, r))

if __name__ == '__main__':
    main()