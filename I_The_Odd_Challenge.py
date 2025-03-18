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
    t = int(input())
    
    for _ in range(t):
        n, q = map(int, input().split())
        a = list(map(int, input().split()))
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + a[i]
        
        total_sum = prefix[-1]
        results = []
        for _ in range(q):
            l, r, k = map(int, input().split())
            replaced_range_old_sum = prefix[r] - prefix[l - 1]
            replaced_range_new_sum = (r - l + 1) * k
            new_sum = total_sum - replaced_range_old_sum + replaced_range_new_sum
            if new_sum % 2 == 1:
                results.append("YES")
            else:
                results.append("NO")
        print("\n".join(results))
def main():
    solve()

if __name__ == '__main__':
    main()
