# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

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

def solve(nums):
    maxi = max(nums)
    ans = []
    a,b,c = nums
    d = nums.count(maxi)
    if d == 3:
        return [1,1,1]
    elif d > 1:
       for i in range(len(nums)):
            if nums[i] == maxi:
                ans.append(1)
            else:
                ans.append(abs(nums[i] - maxi) + 1) 
    else:
        for i in range(len(nums)):
            if nums[i] == maxi:
                ans.append(abs(nums[i] - maxi))
            else:
                ans.append(abs(nums[i] - maxi) + 1)

    return ans



def main():
    t = iinp()
    for _ in range(t):
        nums = linp()
        print(*solve(nums), sep=" ")

if __name__ == '__main__':
    main()