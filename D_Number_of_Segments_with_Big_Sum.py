def number_big_sum(nums, n, s):
   l = 0
   current_sum = 0
   good_segment = 0

   for r in range(n):
       current_sum += nums[r]
       while l < n and current_sum > s:
            current_sum -= nums[l]
            good_segment +=  1
            l += 1             
   return good_segment

def main():
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))  
    print(number_big_sum(nums, n, s))

main()