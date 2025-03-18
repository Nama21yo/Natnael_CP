from __future__ import division, print_function
import itertools
import sys
import os
from collections import defaultdict

if sys.version_info[0] < 3:
    input = raw_input
    range = xrange
    filter = itertools.ifilter
    map = itertools.imap
    zip = itertools.izip

def solve(n, s):
    prefix_sum_count = defaultdict(int)
    prefix_sum_count[0] = 1
    prefix_sum = 0
    good_subarray = 0
    for i,char in enumerate(s):
        prefix_sum += int(char)
        diff = prefix_sum - i - 1
        good_subarray += prefix_sum_count[diff]
        prefix_sum_count[diff] += 1
    return good_subarray

def main():
    t = int(input().strip())
    for _ in range(t):
        string_length = int(input().strip())
        binary_string = input().strip()
        print(solve(string_length, binary_string))


if __name__ == "__main__":
    main()

# from __future__ import division, print_function
# import itertools
# import sys
# import os
# from collections import defaultdict

# if sys.version_info[0] < 3:
#     input = raw_input
#     range = xrange
#     filter = itertools.ifilter
#     map = itertools.imap
#     zip = itertools.izip

# def solve(string_length_and_binary_string):
#     string_length, binary_string = string_length_and_binary_string
#     prefix_sums = [0] * (string_length + 1)

#     for i in range(1, string_length + 1):
#         prefix_sums[i] = prefix_sums[i - 1] + int(binary_string[i - 1])

#     prefix_difference_count = defaultdict(int)

#     for i in range(string_length + 1):
#         difference = prefix_sums[i] - i
#         prefix_difference_count[difference] += 1

#     total_good_subarrays = sum(f * (f - 1) // 2 for f in prefix_difference_count.values())

#     return total_good_subarrays

# def main():
#     test_cases = int(input().strip())
#     results = []

#     for _ in range(test_cases):
#         string_length = int(input().strip())
#         binary_string = input().strip()
#         results.append(str(solve((string_length, binary_string))))

#     print("\n".join(results))

# if __name__ == "__main__":
#     main()
