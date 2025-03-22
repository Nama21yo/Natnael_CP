# Problem: C - Penalty Shootout - https://codeforces.com/gym/596141/problem/C

import sys
import threading

input_fn = lambda: sys.stdin.readline().strip()

def main():

    def solve():
        s = input()
        score1 = 0
        score2 = 0
        k1 = 10
        k2 = 10
        # just let player 1 win and be greedy
        for i in range(10):
            if score1 > (10 - i + 1) // 2:
                k1 = i
                break
            if s[i] == "1":
                if i % 2 == 0:
                    score1 += 1
                else:
                    score1 -= 1

            elif s[i] == "?":
                if i % 2 == 0:
                    score1 += 1
        # just player 2 win and be greedy
        for i in range(10):
            if score2 > (10 - i) // 2:
                k2 = i
                break
            if s[i] == "1":
                if i % 2 == 1:
                    score2 += 1
                else:
                    score2 -= 1

            elif s[i] == "?":
                if i % 2 == 1:
                    score2 += 1
        print(min(k1, k2))
    t = int(input())
    for _ in range(t):
        solve()



if __name__ == '__main__':
    main()
