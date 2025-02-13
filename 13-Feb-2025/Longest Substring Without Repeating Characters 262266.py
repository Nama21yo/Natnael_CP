# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Array to store the last seen index of each character
        last_seen = [-1] * 256  # Initialize an array for 256 ASCII characters
        
        left = 0  # Left pointer for the sliding window
        max_len = 0  # Variable to store the length of the longest substring
        
        # Iterate through the string with the right pointer
        for right in range(len(s)):
            current_char = s[right]
            ascii_value = ord(current_char)  # Get ASCII value of the character
            
            # If the character has been seen, move the left pointer
            if last_seen[ascii_value] != -1:
                left = max(last_seen[ascii_value] + 1, left)
            
            # Update the last seen position of the current character
            last_seen[ascii_value] = right
            
            # Calculate the length of the current substring and update the maximum length
            max_len = max(max_len, right - left + 1)
        
        return max_len  # Return the length of the longest substring
