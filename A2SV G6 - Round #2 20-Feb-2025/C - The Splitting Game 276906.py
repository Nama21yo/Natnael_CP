# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from __future__ import division, print_function
import itertools
import sys
import os

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange

    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def solve(s,n):
    right_count = [0] * 26  
    left_count = [0] * 26   
    # Count distinct characters in the full string
    for ch in s:
        right_count[ord(ch) - ord('a')] += 1

    distinct_right = sum(1 for x in right_count if x > 0)
    distinct_left = 0
    max_sum = 0

    # Iterate through the string and move characters from right to left
    for i in range(n - 1):
        char_index = ord(s[i]) - ord('a')

        # Move this character to the left partition
        if left_count[char_index] == 0:
            distinct_left += 1
        left_count[char_index] += 1

        # Remove from right partition
        right_count[char_index] -= 1
        if right_count[char_index] == 0:
            distinct_right -= 1

        # Update the max distinct sum
        max_sum = max(max_sum, distinct_left + distinct_right)

    return max_sum


def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        s = input().strip()
        print(solve(s, n))

if __name__ == "__main__":
    main()
