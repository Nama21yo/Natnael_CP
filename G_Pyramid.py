def print_pyramid(n, r):
    if r == 0 or n == r:
        print("*")
        return
    return print_pyramid(n - 1, r - 1) + print_pyramid(n - 1, r)

def main():
    n = int(input())  # Read the value of n
    r = n
    # arr = list(map(int, input().split()))  # Read the array
    print_pyramid(n, r)

main()