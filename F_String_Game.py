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
def can_delete(t, index_map, n, mid, p):
    goal =  len(p)
    idx = 0
    for i in range(n):
        if index_map[i] <= mid:
            continue
        elif idx < goal and t[i] == p[idx]:
            idx += 1
    return idx == goal
def solve(t,p, index_map, n):
    l = -1
    r = n + 1
    while r - l > 1:
        mid = l + (r - l)//2
        # TTTTTTT T FFFFFFF patterns
        if can_delete(t,index_map, n , mid, p):
            l = mid
        else:
            r = mid
    return l
def main():
    t = string()
    p = string()
    # map them with their indexes
    n = len(t)
    permutation = linp()
    index_map = [0] * n
    for i in range(1,n + 1):
        x = permutation[i  - 1]
        index_map[x - 1] = i
        # eg. 5 >> "c"
        # put the index of c which is 4 (0-indexed) 
    print(solve(t,p, index_map, n))

if __name__ == '__main__':
    main()