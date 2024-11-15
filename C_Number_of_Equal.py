def number_of_equal(arr1, n, arr2, m):
    l = 0
    h = 0
    count = 0

    while l < n and h < m:
        if arr1[l] == arr2[h]:
            countl = 0
            current_val1 = arr1[l]
            while l < n and arr1[l] == current_val1:
                countl += 1
                l += 1

            counth = 0
            current_val2 = arr2[h]
            while h < m and arr2[h] == current_val2:
                counth += 1
                h += 1

            count += (countl * counth)
        elif arr1[l] < arr2[h]:
            l += 1
        else:
            h += 1

    return count


def main():
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    print(number_of_equal(arr1, n, arr2, m))


main()
