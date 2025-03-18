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
def find_last_bigger(city, towers):
    # bisect right
    # Can also be implemented in two pointers
    l = -1
    r = len(towers)

    while r - l > 1:
        mid = l + (r - l)//2
        if towers[mid] < city: # the valid part
            l = mid
        else:
            r = mid 
    return r

def solve(cities, towers,n,m):
    distance = 0
    for i in range(n):
        # find_first_bigger = bisect_right(towers, cities[i])
        find_first_bigger = find_last_bigger(cities[i], towers)
        
        last_smaller = find_first_bigger - 1

        min_distance = float("inf")
        if find_first_bigger < m: # length of the tower
            min_distance = min(min_distance, towers[find_first_bigger] - cities[i])

        if last_smaller >= 0:
            min_distance = min(min_distance, cities[i] - towers[last_smaller])
        distance = max(distance, min_distance)
    return distance

def main():
    n,m = linp()
    cities = linp()
    towers =  linp()
    print(solve(cities, towers,n,m))

if __name__ == '__main__':
    main()