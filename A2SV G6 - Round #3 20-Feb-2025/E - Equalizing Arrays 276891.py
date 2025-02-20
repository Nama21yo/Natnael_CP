# Problem: E - Equalizing Arrays - https://codeforces.com/gym/588468/problem/E

import sys

def input():
    return sys.stdin.readline().strip()

def int_input():
    return int(input())

def list_input():
    return list(map(int, input().split()))

def solve():
    # Your solution logic here
    n = int_input()
    a = list_input()
    m = int_input()
    b = list_input()

    count = 0
    r1 = r2 = 0

    if a == b:
        return n
    
    while r1 < len(a) and r2 < len(b):
        # Check equality
        if a[r1] == b[r2]:
            r1 += 1
            r2 += 1
            count += 1
        else:
            sum_1 = a[r1]
            sum_2 = b[r2]
            
            while sum_1 != sum_2:
                if sum_1 > sum_2:
                    if r2 + 1 < m:
                        r2 += 1
                        sum_2 += b[r2]
                    else:
                        return -1
                else:
                    if r1 + 1 < n:
                        r1 += 1
                        sum_1 += a[r1]
                    else:
                        return -1
            r1 += 1
            r2 += 1    
            count += 1

    if r1 < n or r2 < m:
        return -1
    
    return count
                    
                

def main():
    ans = solve()
    print(ans)

if __name__ == "__main__":
    main()
