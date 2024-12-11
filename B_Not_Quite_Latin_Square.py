def not_quite_latin_squares(arr, n):
    chars = [-3] * 3
    n = len(arr)
    m = len(arr[0])
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'A':
                chars[0] += 1
            elif arr[i][j] == 'B':
                chars[1] += 1
            elif arr[i][j] == 'C':
                chars[2] += 1
    answer = 65
    for i in range(len(chars)):
        if chars[i] < 0:
            answer += i
    return chr(answer)

def main():
    t = int(input())
    for _ in range(t):
        n = 3
        arr = []
        for _ in range(n):
            start = list(map(str, input().split()))
            row = list(start[0])
            arr.append(row)
        print(not_quite_latin_squares(arr, n))

main()