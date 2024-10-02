def missing_number(arr, n):
    xor1 = 0
    xor2 = 0
    
    for i in range(len(arr)):
        xor1 ^= arr[i]
        xor2 ^= (i + 1)

    xor1 ^= n
    
    return xor1 ^ xor2

def main():
    n = int(input())  
    arr = list(map(int, input().split()))
    print(missing_number(arr, n))

main()
