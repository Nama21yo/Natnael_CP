# Problem: Height Checker
(Easy) - https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count_sort = [0] * (101)

        for num in heights:
            count_sort[num] += 1
        expected = []
        for i,num in enumerate(count_sort):
            while num > 0:
                expected.append(i)
                num -= 1
        
        count_indices = 0
        for height, expect in zip(heights, expected):
            if height != expect:
                count_indices += 1
        return count_indices
