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

def solve(s):
    n = len(s)
    if "".join(s[n-2:]) == "po":
        return "FILIPINO"
    elif "".join(s[n-4:]) == "desu" or "".join(s[n-4:]) == "masu":
        return "JAPANESE"
    return "KOREAN"

def main():
    n = iinp()
    for _ in range(n):
        s = list(string())
        print(solve(s))

if __name__ == '__main__':
    main()