# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count_nums =  Counter(nums)
        pair = 0
        left_over = 0
        for key, value in count_nums.items():
            if value >= 2:
                pair += (value // 2)
            if value % 2 == 1:
                left_over += 1
        print(count_nums)

        return [pair, left_over] 

