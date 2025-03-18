import sys
import threading

def main():
    n = int(input())
    def solve(n):
        if n <= 2:
            return n
        return solve(n - 1) * n
    print(solve(n))

if __name__ == 'main':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
main()
