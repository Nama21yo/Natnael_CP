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
        s = string()

        s1 = 0
        s2 = 0
        m1 = 0
        m2 = 0

        for i in range(10):
            if s1

if __name__ == '__main__':
    sys.setrecursionlimit(1<<30)
    main()
