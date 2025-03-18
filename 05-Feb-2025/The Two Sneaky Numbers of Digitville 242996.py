# Problem: The Two Sneaky Numbers of Digitville - https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count_sneaky = Counter(nums)

        sneaky = []
        for key,count in count_sneaky.items():
            if count == 2:
                sneaky.append(key)
        return sneaky

        