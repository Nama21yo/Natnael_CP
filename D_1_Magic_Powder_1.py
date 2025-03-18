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
def ingredient_needed(needed,have, mid,n, k):
    powder = 0
    for i in range(n):
        powder += max(needed[i]*mid - have[i], 0) # to prevent overflow
        powder = min(powder, k + 1)# to prevent overflow if I have morethan k + 1 I won't able to make cookie
    return powder 

def solve(needed, have, n, k):
    # maximize cookies
    # vvvvvvv iiiiiii return your l
    l = 0
    r = int(3e3)
    while r - l > 1:
        mid = l + (r - l)//2
        # check if the ingriedient is enough
        current_powder = ingredient_needed(needed,have, mid,n, k)
        if current_powder <= k:
            l = mid
        else:
            r = mid
    return l

def main():
    # n = iinp()
    n,k = linp()
    needed = linp()
    have = linp()
    print(solve(needed, have, n, k))

if __name__ == '__main__':
    main()