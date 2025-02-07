# Problem: All Divisions With the Highest Score of a Binary Array - https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/

class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left_zero = 0
        right_one = sum(nums)

        maxi = right_one
        ans = [0]
        for i, num in enumerate(nums, 1):
            left_zero += num ^ 1
            right_one -= num
            score = left_zero + right_one
            if maxi == score:
                ans.append(i)
            if maxi < score:
                maxi = score
                ans = [i]
        return ans

            


        