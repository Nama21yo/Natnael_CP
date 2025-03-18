# Problem: Range Sum Query - Immutable - https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []
        currentSum = 0

        for num in nums:
            currentSum += num
            self.prefixSum.append(currentSum)

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefixSum[right]
        leftSum = self.prefixSum[left - 1] if left > 0 else 0
        return rightSum - leftSum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)