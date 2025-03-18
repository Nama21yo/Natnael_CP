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
    temp = n
    while n % 2 == 0: 
        n = n // 2
    if n == 1:
        return -1
    if temp == 3:
        return -1
    
    return temp - 2 if temp % 2 else temp - 1
def main():
    t = iinp()
    for _ in range(t):
        print(solve())

if __name__ == '__main__':
    main()