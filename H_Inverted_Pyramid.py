def inverted_py_2(n):
    def print_space(x):
       if x == 0:
            return
       print_space(x - 1)
       print(" ", end="")
    def print_star(y):
        if y == 0:
            return
        print("*", end="")
        print_star(y - 1)

    def print_line(row, total_row):
        if row > total_row:
            return
        print_space(row - 1)
        print_star(2 * (total_row - row) + 1)
        print()
        print_line(row + 1, total_row)
       

    if n > 0:
       print_line(1,n)
def inverted_py(n):
    if n <= 0:
        return

    for row in range(1, n + 1):
        # Print spaces
        print(" " * (row - 1), end="")
        # Print stars
        print("*" * (2 * (n - row) + 1))
def pyramid(n):
    if n <= 0:
        return

    for row in range(1, n + 1):
        # Print spaces
        print(" " * (n - row), end="")
        # Print stars
        print("*" * (2 * (row) - 1))

def main():
    n = int(input()) 
    pyramid(n)

main()