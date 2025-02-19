# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

import sys
from collections import Counter

def input():
    return sys.stdin.readline().strip()

def int_input():
    return int(input())

def list_input():
    return list(map(int, input().split()))

def solve():
    # Your solution logic here
    n = int_input()
    s = input()

    counter = set(s)
    ans = n + 1

    for letter in counter:
        res = palindromeChecker(s, letter)
        ans = min(ans, res)
    
    if ans == n + 1:
        print(-1)
    else:
        print(ans)


def palindromeChecker(s, letter):
    left = 0
    right = len(s) - 1
    count = 0

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if s[left] == letter:
                left += 1
                count += 1
            elif s[right] == letter:
                right -= 1
                count += 1
            else:
                return len(s) + 1
    
    return count
    

def main():
    t = int_input()  # Number of test cases
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
