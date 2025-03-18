def print_pyramid(y):
    def print_space(x):
        if x == 0:
            return
        print(" ", end="")
        print_space(x - 1)

    def print_star(n):
        if n == 0:
            return
        print("*", end="")
        print_star(n - 1)

    def print_line(row, total_rows):
        if row > total_rows:
            return
        print_space(total_rows - row)
        print_star(2 * row - 1)
        print()
        print_line(row + 1, total_rows)

    if y > 0:
        print_line(1, y)






def print_triangle_inc(n, i):
    if n == 0:
        return
    if i < n:
        print_triangle_inc(n, i + 1)
        print("*", end=" ")
    else: #i > n
        print_triangle_inc(n - 1, 0)
        print()

def print_triangle_dec(n, i):
    if n == 0:
        return
    # Method 1
    # for i in range(n):
    #     print("*", end=" ")
    # print()
    # print_triangle_dec(n - 1)

    # Method 2
    if i < n:
        # Print the column
        print("*", end=" ")
        print_triangle_dec(n, i + 1)
    else: # i == n
        # change the row
        print()
        print_triangle_dec(n - 1, 0)

def main():
    n = int(input())  # Read the value of n
    # arr = list(map(int, input().split()))  # Read the array
    print_pyramid(n)

main()