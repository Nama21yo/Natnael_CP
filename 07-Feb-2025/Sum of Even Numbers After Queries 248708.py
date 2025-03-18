# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # apply the queries
        even_sum = sum(num for num in nums if num % 2 == 0)
        answer = []
        for val, index in queries:
            even_sum -= nums[index] if nums[index] % 2 == 0 else 0
            nums[index] = nums[index] + val
            even_sum += nums[index] if nums[index] % 2 == 0 else 0
            answer.append(even_sum)
            
        return answer
            
            

    