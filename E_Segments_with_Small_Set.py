def bug_segment(arr, n, k):
    count_map = {}
    l = 0
    good = 0
    
    for r in range(n):
        count_map[arr[r]] = count_map.get(arr[r], 0) + 1

        while len(count_map) > k:
            count_map[arr[l]] -= 1
            if count_map[arr[l]] == 0:
                count_map.pop(arr[l])
            l += 1
        
        good += (r - l + 1)
    
    return good
def main():
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))  
    print(bug_segment(nums, n, k))

main()
