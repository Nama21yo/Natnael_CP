# Problem: Number of Wonderful Substrings - https://leetcode.com/problems/number-of-wonderful-substrings/

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
            ans = 0
            prefix = 0
            count = [0] * 1024  # 2^10 = 1024 possible bitmasks for 10 letters
            count[0] = 1  

            for c in word:
                index = ord(c) - ord('a')
                prefix ^= 1 << index  
                ans += count[prefix]  # Add substrings with even counts for all characters

                # Add substrings where exactly one character has an odd count
                for i in range(10):
                    ans += count[prefix ^ (1 << i)]

                count[prefix] += 1  # Update the count for the current prefix

            return ans