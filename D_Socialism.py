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
    t = iinp()  
    results = []
    for _ in range(t):
        n, x = map(int, input().split())  
        nums = sorted(map(int, input().split()), reverse=True)  # Sort wealth in descending order

        total = 0  
        for i in range(n):
            total += nums[i]  
            if total < x * (i + 1):  # Check if the average wealth falls below x
                results.append(i) 
                break
        else:
            results.append(n)  
    return '\n'.join(map(str, results))  
def main():
    print(solve())

if __name__ == '__main__':
    main()
