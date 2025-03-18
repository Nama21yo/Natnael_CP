import sys

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

def main():
    t = iinp()
    for _ in range(t):
        n = iinp()
        s = string()
        def solve():
            

        print(solve(ord("a"), 0, ))

if __name__ == '__main__':
    sys.setrecursionlimit(1<<30)
    main()
