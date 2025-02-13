# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

def small_sum(nums, n, s):
    l = 0
    r = 0
    current_sum = 0
    max_len = 0
    while r < n:
        current_sum += nums[r]
        while current_sum > s:
            current_sum -= nums[l]
            l += 1
        if current_sum <= s:
            max_len = max(max_len, r - l + 1)
        r += 1
    return max_len


def main():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))  
    print(small_sum(nums, n, s))

main()
