# Problem: D - Creating an a-Good String - https://codeforces.com/gym/596141/problem/D

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

def solve(l,r,c,s):
    if l == r:
        if s[l] == c:
            return 0
        return 1
    
    mid = (l + r) // 2
    
    left_changes = (mid - l + 1) - s[l:mid + 1].count(c)    
    left_result = left_changes + solve(mid + 1, r, chr(ord(c) + 1),s)
    right_changes = (r - mid) - s[mid + 1:r + 1].count(c)
    right_result = right_changes + solve(l, mid, chr(ord(c) + 1), s)
    return min(left_result, right_result)
 
def main():
    t = iinp()
    for _ in range(t):
        n = iinp()
        s = string()
        print(solve(0, len(s) - 1, 'a' ,s))

if __name__ == '__main__':
    main()
