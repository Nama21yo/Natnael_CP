class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        my_set = set(nums)
        for num in nums:
            num = str(num)
            num = num[::-1]
            my_set.add(int(num))
        # print(my_set)
        return len(my_set)
        