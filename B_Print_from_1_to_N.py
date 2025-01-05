def print_n( n):
    if n == 0:
        return
    print_n(n - 1)
    print(n)

def main():
    n = int(input())  # Read the value of n
    print_n(n)

main()