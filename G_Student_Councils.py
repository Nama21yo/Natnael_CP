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
def can_create(mid, nums, n ,k):
    # mid * k >> the total possible
    # min(mid, num) >> contribution on each group
    return sum(min(mid, num) for num in nums) >= mid * k
def solve(nums, k,n):
    l = -1 
    r = int(1e17) + 1
    while r - l > 1:
        mid = l + (r - l)//2
        # TTTTTT T FFFFF monotonicity
        if can_create(mid, nums,n, k):
            l = mid
        else:
            r = mid
    return l

def main():
    k = iinp()
    n = iinp()
    nums = [iinp() for _ in range(n)]
    print(solve(nums, k,n))

if __name__ == '__main__':
    main()