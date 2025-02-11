# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def map_numbers(self, num, mapping):
        # should include this since the number can be 0 but the while
        # condition won't work for  zero
        if num == 0:
            return mapping[0]
        n = len(mapping)
        ans = 0
        unit = 1
        while num > 0:
            ans += mapping[num % 10] * unit
            unit *= 10
            num //= 10
        
        return ans
    
    def counting_sort(self, nums, units):
        n = len(nums)
        count_arr = [0]* 10 # we have only 10 digits

        for num,unmapped_num in nums:
            idx = num // units
            count_arr[idx % 10] += 1
        
        # do the cummulative sum to make it stable
        for i in range(1, 10):
            count_arr[i] += count_arr[i - 1]
        result = [0] * n
        # start from reverse for stability
        for i in range(n - 1, -1,-1):
            idx = nums[i][0] // units
            # remember this one
            result[count_arr[idx % 10] - 1] = nums[i]
            count_arr[idx % 10] -= 1
        
        return result

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        mapped_nums = []
        for num in nums:
            mapped_nums.append((self.map_numbers(num,mapping),num) )
        
        # Use the radix sort
            # >>> make counting sort on each digits

        # the counting sort must be stable
        maxi = max(mapped_nums)[0]
        units = 1
        while maxi // units > 0:
            mapped_nums = self.counting_sort(mapped_nums,units)
            units *= 10

        return [num for mapped, num in mapped_nums]
        