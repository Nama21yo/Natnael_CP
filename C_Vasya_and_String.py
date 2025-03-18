def check(s, k, l):
    dp = [0, 0]  # Counts for 'a' and 'b'
    # Count characters in the first substring
    for i in range(l):
        dp[ord(s[i]) - ord('a')] += 1
    # Check if we can satisfy the condition for the first substring
    if k >= min(dp[0], dp[1]): # I can change one of them
        return True
    # Sliding window to check other substrings
    for i in range(len(s) - l):
        dp[ord(s[i]) - ord('a')] -= 1  # Remove leftmost character
        dp[ord(s[i + l]) - ord('a')] += 1  # Add new rightmost character
        if k >= min(dp[0], dp[1]): # can change one of them
            return True
    return False
def main():
    n, k = map(int, input().split())
    s = input().strip()
    l, r = 1, n
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        if check(s, k, mid):
            ans = max(ans, mid)
            l = mid + 1
        else:
            r = mid - 1
    print(ans)
main()