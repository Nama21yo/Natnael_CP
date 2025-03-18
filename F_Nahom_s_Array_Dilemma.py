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

    prefix = [0]*(n + 1)

    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + nums[i - 1]
    # print(prefix)
    
    # find prev greater
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            idx = stack.pop() 
            left_side = prefix[i] - prefix[idx]
            if left_side > 0:
                # print(i,idx)
                return "NO"
        stack.append(i)
    
    nums = nums[::-1]
    prefix = [0]*(n + 1)

    for i in range(1, n + 1):
        prefix[i] = prefix[i - 1] + nums[i - 1]
    # print(prefix)
    
    # find prev greater
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            idx = stack.pop() 
            left_side = prefix[i] - prefix[idx]
            if left_side > 0:
                # print(i,idx)
                return "NO"
        stack.append(i)
    return "YES"

    
def main():
    t = iinp()
    for _ in range(t):
        print(solve())

if __name__ == '__main__':
    main()