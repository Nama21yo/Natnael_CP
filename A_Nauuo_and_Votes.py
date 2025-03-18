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

def solve(x, y):
    if x == y:
        return 2
    elif x < y:
        return 1
    else:
        return 0

def main():
    x, y, z = linp()
    result = ['+', '-', '0', '?']
    possible = solve(x + z, y) == solve(x, y + z)
    
    if possible:
        index = solve(x, y)
        print(result[index])
    else:
        print(result[3])

if __name__ == "__main__":
    main()
