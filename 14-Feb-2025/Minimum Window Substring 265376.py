# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    # def valid_substring(self, count_t, window):
    #     for char in count_t:
    #         if count_t[char] > window[char]:
    #             return False
    #     return True

# aaaaaaabbbbbcdd
# t>> abcdd
# ANS >> abbbbbcdd
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        n = len(s)
        mini = float("-inf")
        maxi = float("inf")

        count_t = Counter(t)
        count_possible = 0
        # dynamic sliding window
        for r in range(n):
            if s[r] in count_t:
                count_t[s[r]] -= 1
                if count_t[s[r]] >= 0:
                    count_possible += 1
            
            while count_possible == len(t):
                if r - l < maxi - mini:
                    mini  = l
                    maxi = r
                if s[l] in count_t:
                    count_t[s[l]] += 1
                    if count_t[s[l]] > 0:
                        count_possible -= 1
                l += 1
        return s[mini:maxi + 1] if maxi - mini < len(s) else ""