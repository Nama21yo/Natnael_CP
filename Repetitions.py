def count_repetition(s):
    n = len(s)
    max_count = 0
    l = 0

    while l < n:
        r = l
        while r < n and s[l] == s[r]:
            r += 1
        max_count = max(max_count, r - l)
        l = r

    return max_count

def main():
    s = input()
    print(count_repetition(s))

main()
