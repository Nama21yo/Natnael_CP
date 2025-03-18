import sys
import threading

input = lambda: sys.stdin.readline().strip()

def main():
    n = int(input())
    def solve(n):
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        return solve(n - 1) + solve(n - 2)
 
    print(solve(n - 1))

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
