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
    n = iinp()
    binary = list(string())
    stack_0 = []
    stack_1 = []
    subsequence = 0
    ans = [0]*n
    for i in range(n):
        if binary[i] == "0":
            if stack_1:
                val = stack_1.pop()
                stack_0.append(val)
                ans[i] = val
            else:
                subsequence += 1
                stack_0.append(subsequence)
                ans[i] = subsequence
        else:
            if stack_0:
                val = stack_0.pop()
                stack_1.append(val)
                ans[i] = val
            else:
                subsequence += 1
                stack_1.append(subsequence)
                ans[i] = subsequence
    return [subsequence, ans]

def main():
    t = iinp()
    for _ in range(t):
        maxi, ans = solve()
        print(maxi)
        print(*ans)

if __name__ == '__main__':
    main()