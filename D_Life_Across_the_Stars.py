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

def solve(logs,n):
    line = defaultdict(int)
    for birth, death in logs:
        line[birth] += 1
        line[death] -= 1
    max_year = 0
    running_sum = 0
    count = 0
    
    for year in sorted(line.keys()):
        running_sum += line[year]
        if running_sum > count:
            max_year = year
            count = running_sum
    return [max_year,count]
def main():
    n = iinp()
    logs  = []
    for _ in range(n):
        row = linp()
        logs.append(row)
    # nums = linp()
    print(*solve(logs, n))

if __name__ == '__main__':
    main()