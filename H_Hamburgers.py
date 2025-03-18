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
def can_prepare(mid, burger_type, nb, ns,nc,pb, ps, pc, money):
    # count the bread, sausage and cheese needed
    count_b = burger_type.count("B")
    count_s = burger_type.count("S") 
    count_c = burger_type.count("C")
    # neeeded  B,S,C for that hamburger
    for_b = mid*count_b
    for_s = mid*count_s
    for_c = mid*count_c
    # count extra needed price
    extra_price = 0
    extra_price += max((for_b - nb), 0) * pb # the extra bread price 
    extra_price += max((for_s - ns), 0) * ps 
    # make max 0 for not making it -ve
    # >> it means we already have enough ingredients, so the extra price should not decrease our total money.
    extra_price += max((for_c - nc), 0) * pc
    return extra_price <= money # the extra price should be at most my money I have 

def solve(burger_type, nb, ns,nc,pb, ps, pc, money):
    l  = - 1
    r = int(1e15) + 1
    # maximize hamburger
    # TTTTTTTTT T FFFFFFF pattern
    while r - l > 1:
        mid = l + (r - l)//2
        if can_prepare(mid, burger_type, nb, ns,nc,pb, ps, pc, money):
            l = mid
        else:
            r = mid
    return l # can prepare l hamburgers
def main():
    burger_type = list(string())
    nb , ns, nc = linp()
    pb, ps, pc = linp()
    money = iinp()
    print(solve(burger_type, nb, ns,nc,pb, ps, pc, money))

if __name__ == '__main__':
    main()