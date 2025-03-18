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
    h, w = map(int, input().split())
    grid = []
    for i in range(h):
        grid.append(input())
    horizontal = [[0] * w for _ in range(h)]
    vertical = [[0] * w for _ in range(h)]

    for r in range(h):
        for c in range(w):
            if c > 0 and grid[r][c] == grid[r][c - 1] == '.':
                horizontal[r][c] = 1

            if r > 0 and grid[r][c] == grid[r - 1][c] == '.':
                vertical[r][c] = 1

    for r in range(h):
        for c in range(1, w):
            horizontal[r][c] += horizontal[r][c - 1]
            vertical[r][c] += vertical[r][c - 1]

    for c in range(w):
        for r in range(1, h):
            horizontal[r][c] += horizontal[r - 1][c]
            vertical[r][c] += vertical[r - 1][c]

    q = int(input())

    for i in range(q):
        r1, c1, r2, c2 = map(int, input().split())
        r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1 # changing 1-indexed input to 0-indexed

        horizontal_count = horizontal[r2][c2] - horizontal[r2][c1]
        if r1 - 1 >= 0:
            horizontal_count += horizontal[r1 - 1][c1] - horizontal[r1 - 1][c2]

        vertical_count = vertical[r2][c2] - vertical[r1][c2]
        if c1 - 1 >= 0:
            vertical_count += vertical[r1][c1 - 1] - vertical[r2][c1 - 1]

        answer = horizontal_count + vertical_count

        print(answer)

def main():
    solve()

if __name__ == '__main__':
    main()
