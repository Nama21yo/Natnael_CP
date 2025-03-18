# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

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

def solve(temp_interval, question,n,k):
    l ,r = question
    # count_temp = 0
    # for i in range(l, r + 1):
    #     if temp_interval[i] > k:
    #         count_temp += 1
    return temp_interval[r] - temp_interval[l - 1]


    

def main():
    n, k, q = linp()
    recipes = []
    for _ in range(n):
        recipe = linp()
        recipes.append(recipe)
    temp_interval = [0]* (2000001)
    for l, r in recipes:
        temp_interval[l] += 1
        temp_interval[r + 1] -= 1
    temp_interval[0] = 1
    for i in range(1, 2000001):
        temp_interval[i] = temp_interval[i - 1] + temp_interval[i]
    
    # >> Update the diifference array so that the conditon mets
    for i in range(2000001):
        temp_interval[i] = 1 if temp_interval[i] > k else 0
    
    # Do again prefix sum
    temp_interval[0] = 1
    for i in range(1, 2000001):
        temp_interval[i] = temp_interval[i - 1] + temp_interval[i]

    for _ in range(q):
        question = linp()
        print(solve(temp_interval, question,n,k))

if __name__ == '__main__':
    main()