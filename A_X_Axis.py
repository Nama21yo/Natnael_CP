def find_smallest(nums):
    nums.sort()
    # 1 5 9 = (5 - 1) + (9 - 5) = 8
    return abs(nums[1] - nums[0]) + abs(nums[2] - nums[1])

def main():
    t = int(input()) 
    for _ in range(t):
        arr = list(map(int, input().split()))  
        print(find_smallest(arr))

main()
