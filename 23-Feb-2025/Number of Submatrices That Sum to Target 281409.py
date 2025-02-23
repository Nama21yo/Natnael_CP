# Problem: Number of Submatrices That Sum to Target - https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        count_target = 0
        for row1 in range(n):
            prefix = [0] * m  
            for row2 in range(row1, n):  
                for col in range(m):
                    prefix[col] += matrix[row2][col]  
                count_target += self.subarraySum(prefix, target)
        return count_target
    def subarraySum(self, nums, target):
        # prefixsum HashMap technique
        prefix_sum = 0
        count = 0
        prefix_map = defaultdict(int)
        prefix_map[0] = 1 # don't forget it
        for num in nums:
            prefix_sum += num
            if (prefix_sum - target) in prefix_map:
                count += prefix_map[prefix_sum - target]
            prefix_map[prefix_sum] += 1
        return count
