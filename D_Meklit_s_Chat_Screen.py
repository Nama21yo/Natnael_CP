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
    n, k = linp()
    nums = linp()

    set_num = set()
    queue = deque()
    for num in nums:
        if num not in set_num:
            if len(queue) == k:
                val = queue.popleft()
                set_num.remove(val)
                # add it
                queue.append(num)
                set_num.add(num)
            else:
                queue.append(num)
                set_num.add(num)
        else:
            if len(queue) == k and num not in set_num:
                val = queue.popleft()
                set_num.remove(val)
                # add it
                queue.append(num)
                set_num.add(num)
    return [len(queue),list(reversed(list(queue)))]
def main():
    len, arr = solve()
    print(len)
    print(*arr)

if __name__ == '__main__':
    main()