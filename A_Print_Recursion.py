def print_recursion(n):
    if n == 0:
        return
    print_recursion(n - 1)
    print("I love Recursion")

def main():
    n = int(input()) 
    print_recursion(n)

main()