# Problem: Tuple with Same Product - http://leetcode.com/problems/tuple-with-same-product

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product_count = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                possible_product = nums[i] * nums[j]
                product_count[possible_product] += 1
        
        # pairs = XC2. , x = value, number of ways to choose 2 pairs
        # xC2 = x * x - 1  // 2

        ans = 0
        for value in product_count.values():
            pairs = (value * (value - 1)) // 2
            ans += pairs * 8

        return ans
        