# Problem: Count Number of Distinct Integers After Reverse Operations - https://leetcode.com/problems/count-number-of-distinct-integers-after-reverse-operations/

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        my_set = set(nums)
        for num in nums:
            num = str(num)
            num = num[::-1]
            my_set.add(int(num))
        # print(my_set)
        return len(my_set)
        