# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums):
        candidates = self.findCandidate(nums)
        return self.validateCandidates(nums, candidates)
    
    def findCandidate(self, nums):
        count1, count2 = 0, 0
        cand1, cand2 = None, None
        
        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0 and num != cand2:
                cand1 = num
                count1 = 1
            elif count2 == 0 and num != cand1:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        
        return [cand1, cand2]
    
    def validateCandidates(self, nums, candidates):
        count1, count2 = 0, 0
        cand1, cand2 = candidates[0], candidates[1]
        
        # Count occurrences of the two candidates
        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1
        
        ans = []
        mini = len(nums) // 3
        
        # Only add the candidates if their counts exceed n/3
        if count1 > mini:
            ans.append(cand1)
        if count2 > mini and cand2 != cand1:  # Avoid duplicates
            ans.append(cand2)
        
        return ans
