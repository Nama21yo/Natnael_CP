# Problem: F - The Last Problem - https://codeforces.com/gym/591928/problem/F

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
    a = linp()
    b = linp()

    pre = [0]*(n + 1)
    for i in range(n):
        pre[i + 1] = pre[i] + a[i] * b[i] 
    
    total = pre[-1]
    ans = total
    # take all as the mid
    for i in range(n):
        l = i - 1
        r = i + 1
        prod = a[i]*b[i]
        while l >= 0 and r < n: # odd expand
            prod += a[r] * b[l]
            prod += a[l] * b[r] # reversed
            ans = max(ans, prod + pre[l] + (total - pre[r + 1]))
            l -= 1
            r += 1
        
        prod = 0
        l = i
        r = i + 1
        while l >= 0 and r < n: # even expand
            prod += a[r] * b[l]
            prod += a[l] * b[r] # reversed
            ans = max(ans, prod + pre[l] + (total - pre[r + 1]))
            l -= 1
            r += 1
    return ans

def main():
    print(solve())

if __name__ == '__main__':
    main()