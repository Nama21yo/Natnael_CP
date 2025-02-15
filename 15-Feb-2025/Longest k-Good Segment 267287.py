# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

import sys
from collections import defaultdict

def solve(n, k, a):
    freq = defaultdict(int)
    l = 0
    distinct = 0
    max_len = 0
    best_l, best_r = 0, 0

    for r in range(n):
        if freq[a[r]] == 0:
            distinct += 1
        freq[a[r]] += 1

        while distinct > k:
            freq[a[l]] -= 1
            if freq[a[l]] == 0:
                distinct -= 1
            l += 1

        if r - l + 1 > max_len:
            max_len = r - l + 1
            best_l, best_r = l + 1, r + 1 

    print(best_l, best_r)

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    solve(n, k, a)

if __name__ == "__main__":
    main()
