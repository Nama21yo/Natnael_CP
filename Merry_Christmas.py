def merry_christmas(n):
    tasks = [1,2,4]
    count = 0
    for task in tasks:
        if n >= task:
            n -= task
            count += 1
        else:
            break

    return count


def main():
    n = int(input()) 
    print(merry_christmas(n))

main()