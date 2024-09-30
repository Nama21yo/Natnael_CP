def main():
    import sys
    input = sys.stdin.read
    
    data = input().splitlines()  # Read all input at once
    t = int(data[0])  # First line contains the number of test cases
    results = []

    index = 1
    for _ in range(t):
        n = int(data[index])  # Number of fruits
        index += 1
        x, y = map(int, data[index].split())  # Blender capacity and input rate
        index += 1

        if n == 0:
            results.append(0)  # If no fruits, time is 0
            continue

        # Calculate minimum time needed
        min_time = (n + y - 1) // y  # Time to fill the blender
        blended_time = (n + x - 1) // x  # Time to blend all fruits

        # Append the maximum of the two times to results
        results.append(max(min_time, blended_time))

    # Output all results
    for result in results:
        print(result)

if __name__ == '__main__':
    main()
