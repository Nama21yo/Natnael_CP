# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

def count_good_numbers(n):
    count = 0
    for i in range(n + 1):
        # Define the condition for a "good number"
        if i % 2 == 0 and i % 5 == 0:  # Example: divisible by both 2 and 5
            count += 1
    return count

# Example usage
n = 100
print(f"Count of good numbers between 0 and {n}: {count_good_numbers(n)}")
