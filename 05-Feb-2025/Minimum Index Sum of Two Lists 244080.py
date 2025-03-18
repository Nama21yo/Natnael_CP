# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_string = defaultdict(int)

        for i,string in enumerate(list1):
            common_string[string] = i
          
        
        min_index = float("inf")
        ans = []
        for i, string in enumerate(list2):
            if string in common_string:
                index_sum = i + common_string[string]
                if index_sum < min_index:
                    min_index = index_sum
                    ans = [string] # found my least sum index
                    # intial it again with new string forgetting the rest
                elif index_sum == min_index:
                    ans.append(string)
        
        return ans