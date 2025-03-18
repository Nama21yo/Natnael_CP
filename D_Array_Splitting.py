# import itertools
# from collections import Counter, defaultdict, deque
# from bisect import bisect_right, bisect_left
# from math import ceil, sqrt

# def gcd(x, y):
#     while y:
#         x, y = y, x % y
#     return x

# def iinp():
#     return int(input().strip())

# def linp():
#     return list(map(int, input().strip().split()))

# def string():
#     return input().strip()

# def lsinp():
#     return input().strip().split()

# def digit():
#     return [int(i) for i in input().strip()]

# def character():
#     return list(input().strip())

# def solve():
#     n, k = linp()
#     nums = linp()

#     cost = nums[0]
#     i = 1
#     factor = 1
#     while i < n:
#         if nums[i] <= 0:
#             cost += nums[i] * factor
#             if n - i >= k - factor:
#                 factor += 1
#         else: # for positive
#             if factor < k:
#                 factor += 1
#             cost += nums[i] * factor
#         i += 1
#     return cost

# def main():
#     print(solve())

# if __name__ == '__main__':
#     main()
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    sum_val = 0
    v = []
    
    # Calculate the suffix sum and store it in v
    for i in range(n - 1, -1, -1):
        sum_val += a[i]
        if i > 0:
            v.append(sum_val)
    
    res = sum_val

    # Sort v in descending order
    v.sort(reverse=True)

    # Add the top (k-1) values from v to res
    for i in range(k - 1):
        res += v[i]

    print(res)

if __name__ == "__main__":
    main()
