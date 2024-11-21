def big_sum(nums, n, s):
    l = 0
    current_sum = 0
    good_segments = 0
    #! The Dynamic Sliding Window Template

    # Using the for-while loop combo
    
    # for loop for the right
        # Update right
        #! while loop for the left pointer validating
            # l++
            # update your answer for true value
        # update your answer for falsy value
    
    for r in range(n):
        current_sum += nums[r]
        while current_sum > s:
            current_sum -= nums[l]
            l += 1
        
        good_segments += (r - l + 1)
    return good_segments


def main():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))  
    print(big_sum(nums, n, s))

main()
