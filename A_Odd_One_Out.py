def odd_one_out(arr, n):
    xor_unique = 0
    for num in arr:
        xor_unique = xor_unique ^ num
    return xor_unique
def main():
    n = int(input())
    for _ in range(n):
        arr = list(map(int, input().split()))  # Read the array
        print(odd_one_out(arr, n))
main()