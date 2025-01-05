def print_n1(n):
    if n == 1:
        print(n)
        return
    print(n, end=" ")
    print_n1(n - 1)


def main():
    n = int(input()) 
    print_n1(n)

main()