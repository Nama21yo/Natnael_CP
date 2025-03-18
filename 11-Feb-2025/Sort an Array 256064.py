# Problem: Sort an Array - https://leetcode.com/problems/sort-an-array/description/

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        count_arr = [0] * (2 * 5 * 10 ** 4 + 1)
        
        for num in nums:
            # we add 5 * 10^4 because for smallest possible element -5 * 10^4 index must be 0
            count_arr[num + 5 * 10**4] += 1
        j = 0
        for num, freq in enumerate(count_arr):
            while freq != 0:
                nums[j] = num - 5 * 10**4
                j += 1
                freq -= 1

        return nums