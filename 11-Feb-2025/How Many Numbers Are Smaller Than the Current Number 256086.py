# Problem: How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count_arr = [0] * 101

        for num in nums:
            count_arr[num] += 1
        
        for i in range(1, 101):
            count_arr[i] = count_arr[i - 1] + count_arr[i]

        # the prefix sum will have the smallest number before it
        ans = []

        for i in range(n):
            if nums[i] == 0:
                ans.append(0)
            else:
                ans.append(count_arr[nums[i] - 1])
        return ans


        