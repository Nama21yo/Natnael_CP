# Problem: Runner-up Score - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    maxi = float("-inf")
    second_maxi = float("inf")
    
    for i in range(n):
        if arr[i] > maxi:
            second_maxi = maxi
            maxi = arr[i]
        elif arr[i] > second_maxi and arr[i] != maxi:
            second_maxi = arr[i]
    print(second_maxi)