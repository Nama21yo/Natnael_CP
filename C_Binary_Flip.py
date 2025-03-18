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
    A = input().strip() 
    B = input().strip() 
    
    A += '0' 
    B += '0' 
    count = 0  
    
    for i in range(n):
        # if count == 0, it means we have equal 1s and 0s
        if A[i] == '1':
            count += 1
        else:
            count -= 1
        
        if count != 0:
            # if the characters differ and next characters are the same, it's impossible
            if A[i] != B[i] and A[i+1] == B[i+1]:
                print("NO")
                return
            
            # if current characters are the same, but next characters differ, it's impossible
            elif A[i] == B[i] and A[i+1] != B[i+1]:
                print("NO")
                return
    print("YES")

def main():
    t = iinp()  
    for _ in range(t):
        solve()  

if __name__ == '__main__':
    main()
