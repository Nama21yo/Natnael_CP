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

def solve(en,x):
    
    num_ice = x
    num_kid = 0
    for sign, val in en:
        if sign == "+":
            num_ice += int(val)
        else:
            if num_ice - int(val) < 0:
                num_kid += 1
                continue
            num_ice = num_ice - int(val) 
    return (num_ice, num_kid)


def main():
    # n = iinp()
    n , x = linp()

    en = []
    for _ in range(n):
        y = list(map(str, input().strip().split()))
        en.append(y)
    print(*solve(en,x))

if __name__ == '__main__':
    main()
