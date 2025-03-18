# Problem: Count Vowel Strings in Ranges - https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix = [0]*(n + 1)
        vowels = set("aeiou")
        for i,word in enumerate(words):
            if word[0] in vowels and word[len(word) - 1] in vowels:
                prefix[i + 1] = 1
            else:
                prefix[i + 1] = 0
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + prefix[i]
        ans = []
        # print(prefix)
        for l, r in queries:

            # print(prefix[r + 1], prefix[l])
            ans.append(prefix[r + 1] - prefix[l])
        return ans

