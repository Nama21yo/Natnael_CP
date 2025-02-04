# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_count = Counter(nums)
        k_freq = my_count.most_common(k) # tuple is returned
        
        return [i for i,j in k_freq]

        