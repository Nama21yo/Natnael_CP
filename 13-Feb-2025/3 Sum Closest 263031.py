# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        min_diff = float("inf")
        result = float("inf")
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                current_diff = abs((nums[i] + nums[l] + nums[r]) - target)
                if current_diff < min_diff:
                    min_diff = current_diff
                    result = (nums[i] + nums[l] + nums[r])

                if nums[i] + nums[l] + nums[r] > target:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    return target
                    l += 1
                    r -= 1
            
        return result