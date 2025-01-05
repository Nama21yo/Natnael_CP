def print_indices(arr, i, n):
    if i == n:
        return
    print_indices(arr, i + 1, n)
    if i % 2 == 0:
        print(arr[i], end = " ")

def main():
    n = int(input())  
    arr = list(map(int, input().split())) 
    i = 0
    print_indices(arr, i, n)

main()
# other method
def print_indices(arr, i, n):
    if i == n:
        return
    print_indices(arr, i + 1, n)
    if i % 2 == 0:
        print(arr[i], end = " ")

def main():
    n = int(input())  
    arr = list(map(int, input().split())) 
    i = 0
    print_indices(arr, i, n)

main()
