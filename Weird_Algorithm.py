def weird_algorithm(n):
    while n > 1:
        print(n, end=' ')  # Print the current value of n without a newline
        if n % 2 == 0:
            n //= 2  # Use integer division for even n
        else:
            n = 3 * n + 1  # Calculate the new value for odd n
    print(n)  # Print the last value, which will be 1

# Read input from the user
n = int(input())
weird_algorithm(n)
