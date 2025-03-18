# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

# TC - O(nlogn) due to sorting
# SC - O(n)
def less_or_equal(arr,n, k):
    arr.sort()
    if k == 0:
        return -1 if arr[0] == 1 else 1
    if n == k:
        return arr[k - 1]

    if arr[k - 1] == arr[k]:
        return -1

    return arr[k] - 1

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(less_or_equal(arr, n ,k))

main()

