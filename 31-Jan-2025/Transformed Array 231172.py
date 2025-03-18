# Problem: Transformed Array - https://leetcode.com/problems/transformed-array/description/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums[i] == 0:
                result.append(nums[i])
            else:
                # Remainder is best when it is circular array
                result.append(nums[(nums[i] + i) % len(nums)])
        return result