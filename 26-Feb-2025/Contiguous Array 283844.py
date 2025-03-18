# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_seen = defaultdict(int)
        # don't forget to put - 1 as intializer
        count_seen[0] = -1
        count = 0
        ans = 0
        for i,num in enumerate(nums):
            if num == 0:
                count -= 1
            if num == 1:
                count += 1
            # print(count_seen)
            if count in count_seen:
                ans = max(ans, i - count_seen[count])
            else:
                count_seen[count] = i
        return ans