# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        good_string_len = 0
        char_map = Counter(chars)

        for word in words:
            temp_count = char_map.copy()
            can_be_word = True
            for char in word:
                if temp_count[char] <= 0:
                    can_be_word = False
                    break
                temp_count[char] -= 1
            
            if can_be_word:
                good_string_len += len(word)
                
        return good_string_len

        