# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

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
    n, k = linp()
    nums = linp()

    max_deque = deque()
    min_deque = deque()

    l = 0
    count_sub = 0
    for r in range(n):
        # max >> monotonic increasing / min at first 
        while max_deque and nums[max_deque[-1]] > nums[r]:
            max_deque.pop()
        max_deque.append(r)
        # min >> monotonic decreasing / max at first
        while min_deque and nums[min_deque[-1]] < nums[r]:
            min_deque.pop()
        min_deque.append(r)
        
        while l < n and max_deque and min_deque and nums[min_deque[0]] - nums[max_deque[0]] > k:
            if max_deque and nums[max_deque[0]] == nums[l]:
                max_deque.popleft()
            if min_deque and nums[min_deque[0]] == nums[l]:
                min_deque.popleft()
            l += 1
        
        count_sub += r - l + 1
    return count_sub
def main():
    # n = iinp()
    print(solve())

if __name__ == '__main__':
    main()
