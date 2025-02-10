# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        count_freq = Counter(s)

        ans = []
        for key, value in reversed(sorted(count_freq.items(), key=lambda x : x[1])):
            while count_freq[key] > 0:
                ans.append(key)
                count_freq[key] -= 1
        return "".join(ans)
        