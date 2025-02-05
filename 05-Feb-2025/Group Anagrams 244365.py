# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_anagram = defaultdict(list)
        
        for string in strs:
            key_count = [0]*26
            for char in string:
                key_count[ord(char) - ord("a")] += 1
            count_anagram[tuple(key_count)].append(string)
        
        return [value for key, value in count_anagram.items()]