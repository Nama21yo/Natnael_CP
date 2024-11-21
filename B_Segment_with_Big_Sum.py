def big_sum(nums, n, s):
    l = 0
    r = 0
    current_sum = 0
    min_len = float("inf")
    #! The Dynamic Sliding Window Template

    # Using the for while loop combo
    # for loop for the right
        # Update right
        #! while loop for the left pointer validating
            # l++
            # update your answer for true value
        # update your answer for falsy value
    
    for r in range(n):
        current_sum += nums[r]
        while current_sum >= s:
            current_sum -= nums[l]
            min_len = min(min_len, r - l + 1)
            l += 1
    return min_len if min_len != float("inf") else -1


def main():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))  
    print(big_sum(nums, n, s))

main()
