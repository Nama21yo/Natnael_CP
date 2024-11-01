# Using Binary Search
def max_piece_length(ropes, n, k):
    low, high = 0 , max(ropes)
    epsilon = 1e-7  

    while high - low > epsilon:
        mid = (low + high) / 2
        pieces = sum(int(rope / mid) for rope in ropes)

        if pieces >= k:
            low = mid  
        else:
            high = mid  

    return low

def main():
    n, k = map(int, input().split())  
    ropes = [int(input()) for _ in range(n)] 
    result = max_piece_length(ropes, n, k)
    print(result)  

main()
