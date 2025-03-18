Scenario 1: Largest Number (LeetCode 179 - Medium)
Problem Statement
Given a list of non-negative integers, arrange them to form the largest possible number.

🔹 Example

python
Copy
Edit
Input: [3, 30, 34, 5, 9]
Output: "9534330"
🔹 Key Idea:
Instead of sorting numerically, we sort numbers based on their concatenation.

Solution Using Custom Comparator
python
Copy
Edit
from functools import cmp_to_key

def largest_number_compare(x, y):
    return -1 if x + y > y + x else 1

def largest_number(nums):
    str_nums = list(map(str, nums))
    sorted_nums = sorted(str_nums, key=cmp_to_key(largest_number_compare))
    
    # Edge case: If the largest number is "0", return "0"
    if sorted_nums[0] == "0":
        return "0"
    
    return "".join(sorted_nums)

# Test
print(largest_number([10, 2]))         # Output: "210"
print(largest_number([3, 30, 34, 5, 9]))  # Output: "9534330"
💡 Why It Works?

We compare x + y vs y + x, ensuring that the order forms the largest concatenated number.
Scenario 2: Custom Sorting by Frequency (LeetCode 451 - Medium)
Problem Statement
Given a string s, sort its characters by frequency in descending order.

🔹 Example

python
Copy
Edit
Input: "tree"
Output: "eert"  # Since 'e' appears twice, it comes first.
🔹 Key Idea:
Sort characters based on their frequency, using a custom comparator.

Solution Using Custom Comparator
python
Copy
Edit
from collections import Counter
from functools import cmp_to_key

def frequency_sort(s):
    freq = Counter(s)
    
    def compare(x, y):
        return freq[y] - freq[x]  # Sort descending by frequency
    
    sorted_chars = sorted(freq.keys(), key=cmp_to_key(compare))
    
    return "".join(char * freq[char] for char in sorted_chars)

# Test
print(frequency_sort("tree"))  # Output: "eert"
print(frequency_sort("cccaaa"))  # Output: "aaaccc"
💡 Why It Works?

The comparator sorts descending by frequency (freq[y] - freq[x]).
Scenario 3: Largest Perimeter Triangle (LeetCode 976 - Easy)
Problem Statement
Given an array of numbers, find the largest perimeter of a triangle that can be formed using any three numbers.

🔹 Example

python
Copy
Edit
Input: [2, 1, 2]
Output: 5
🔹 Key Idea:
To form a triangle with sides (a, b, c), they must satisfy:

𝑎
+
𝑏
>
𝑐
a+b>c
Sort the array in descending order and check the first valid triplet.

Solution Using Custom Comparator
python
Copy
Edit
from functools import cmp_to_key

def largest_perimeter(nums):
    def compare(x, y):
        return y - x  # Sort in descending order
    
    nums.sort(key=cmp_to_key(compare))
    
    for i in range(len(nums) - 2):
        if nums[i] < nums[i+1] + nums[i+2]:
            return nums[i] + nums[i+1] + nums[i+2]
    return 0

# Test
print(largest_perimeter([2, 1, 2]))  # Output: 5
print(largest_perimeter([1, 2, 1, 10]))  # Output: 0 (No valid triangle)
💡 Why It Works?

Sorting in descending order ensures we check the largest perimeter first.
Scenario 4: Sorting by Last Digit (Codeforces Custom Problem)
Problem Statement
Given a list of numbers, sort them based on their last digit in ascending order.

🔹 Example

python
Copy
Edit
Input: [19, 23, 45, 62, 81]
Output: [62, 23, 45, 81, 19]  # Sorted by last digit: 2, 3, 5, 1, 9
🔹 Key Idea:
Sort numbers by their last digit.

Solution Using Custom Comparator
python
Copy
Edit
from functools import cmp_to_key

def sort_by_last_digit(nums):
    def compare(x, y):
        return (x % 10) - (y % 10)  # Compare last digits
    
    return sorted(nums, key=cmp_to_key(compare))

# Test
print(sort_by_last_digit([19, 23, 45, 62, 81]))  # Output: [62, 23, 45, 81, 19]
💡 Why It Works?

Sorting based on x % 10 arranges numbers by their last digit.
