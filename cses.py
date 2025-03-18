def solve(N, songs):
    start = 0
    ans = 0
    # Dictionary to store the last occurrence index of each song
    mp = {}

    # Iterate through the songs list
    for end in range(N):
        # If the current song is not present in the dictionary
        if songs[end] not in mp:
            mp[songs[end]] = end
        else:
            # If the current song is present in the dictionary and within the window
            if mp[songs[end]] >= start:
                start = mp[songs[end]] + 1
            # Update the last occurrence of the current song to the current index
            mp[songs[end]] = end
        # Update 'ans' to store the maximum length of the range of unique values
        ans = max(ans, end - start + 1)
    return ans


def main():
    # Sample Input
    N = 8
    songs = [1, 2, 1, 3, 2, 7, 4, 2]

    print(solve(N, songs))


if __name__ == "__main__":
    main()
# There is a street of length X whose positions are numbered 0,1 ... X. Initially there are no traffic lights, but N sets of traffic lights are added to the street one after another denoted by P[]. Your task is to calculate the length of the longest passage without traffic lights after each addition.


# Python program for the above approach
from collections import defaultdict

def solve(X, N, P):
    # to store ranges
    ranges = [(0, X)]
    # to store range lengths
    range_lengths = defaultdict(int)
    range_lengths[X] = 1

    for i in range(N):
        pos = P[i]
        # find the range in which pos lies
        it = None
        for r in ranges:
            if r[0] <= pos <= r[1]:
                it = r
                break

        start, end = it

        # Remove range [start, end] from ranges
        ranges.remove(it)
        # Remove length of range [start, end] from the range_lengths
        length = range_lengths[end - start]
        if length == 1:
            del range_lengths[end - start]
        else:
            range_lengths[end - start] = length - 1

        # Insert the new ranges
        ranges.append((start, pos))
        ranges.append((pos, end))
        range_lengths[pos - start] += 1
        range_lengths[end - pos] += 1

        # Print the last element of map as the answer
        print(max(range_lengths.keys()))

X = 8
N = 3
P = [3, 6, 2]
solve(X, N, P)

# This code is contributed by Susobhan Akhuli

# Function to count the number of subarrays divisible by N
def solve(arr, N):
    # Dictionary to store the frequency of prefix sums % N
    remainders_cnt = {0: 1}
    remainder = 0
    cnt = 0

    # Iterate over all the indices and add the count of
    # subarrays with sum divisible by N
    for i in range(len(arr)):
        # Since arr[i] can be negative, we add N to the
        # remainder to avoid negative remainders
        remainder = ((remainder + arr[i]) % N + N) % N
        cnt += remainders_cnt.get(remainder, 0)
        remainders_cnt[remainder] = remainders_cnt.get(remainder, 0) + 1

    return cnt

if __name__ == "__main__":
    # Sample Input
    N = 5
    arr = [1, 2, 3, 4, 5]

    print(solve(arr, N))

from collections import defaultdict

def solve(arr, N, K):
    # left and right pointers to mark the start and end of
    # the sliding window
    left = 0
    right = 0
    # Variable to count how many different numbers we have
    # in the window
    distinct_count = 0
    # Variable to store the final result
    result = 0

    # Dictionary to keep track of how many times each number
    # appears in the window
    frequency = defaultdict(int)

    # Slide the window till the window till the right
    # pointer does not reach the end of the array
    while right < N:
        # Check if the current number is new or if its
        # count is zero
        if frequency[arr[right]] == 0:
            distinct_count += 1

        # Update the count of the current number
        frequency[arr[right]] += 1

        # If there are more than K distinct numbers, shrink
        # the window from the left
        while distinct_count > K:
            # Decrease the count of the number going out of
            # the window
            frequency[arr[left]] -= 1
            # If its count becomes zero, then there will be
            # one less distinct number in the window
            if frequency[arr[left]] == 0:
                distinct_count -= 1
            # Move the left pointer to the right to shrink
            # the window
            left += 1

        # Calculate the number of subarrays that end at the
        # current position
        result += right - left + 1

        # Move the right edge of the window to the right to
        # expand it
        right += 1

    # Return the result
    return result

N = 5
K = 2
arr = [1, 2, 1, 2, 3]

print(solve(arr, N, K))



# Function to check if we can divide the array arr[] into K
# subarrays such that each subarray has sum <= mid
def is_valid(arr, N, K, mid):
    partitions = 1
    running_sum = 0
    # find the number of subarrays such that each subarray
    # has sum <= mid
    for i in range(N):
        running_sum += arr[i]
        if running_sum > mid:
            running_sum = arr[i]
            partitions += 1
    # if the number of subarrays is less than or equal to
    # K, then it means that it is possible to divide arr[]
    # into K subarrays with sum of each subarray <= mid
    return partitions <= K

# function to minimize the maximum sum among all subarrays
def solve(arr, N, K):
    # Define the lower and upper limit of our answer
    low = max(arr)
    high = sum(arr)
    ans = 0
    # Binary Search to minimize the maximum sum
    while low <= high:
        mid = (low + high) // 2
        # If it is possible to divide the array arr[] into
        # K subarrays such that each subarray has sum <=
        # mid, then we update ans and move high to mid-1
        if is_valid(arr, N, K, mid):
            ans = mid
            high = mid - 1
        # If it is impossible to divide the array arr[]
        # into K subarrays such that each subarray has sum
        # <= mid, move low to mid+1
        else:
            low = mid + 1
    return ans

# Sample Input
N = 5
K = 3
arr = [2, 4, 7, 3, 5]

print(solve(arr, N, K))

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # To store the medians
        medians = []

        # To keep track of the numbers that need to be removed from the heaps
        outgoing_num = {}

        # Max heap
        small_list = []

        # Min heap
        large_list = []

        # Initialize the max heap by multiplying each element by -1
        for i in range(k):
            heappush(small_list, -nums[i])

        # Transfer the top 50% of the numbers from max heap to min heap
        # while restoring the sign of each number
        for i in range(k // 2):
            element = heappop(small_list)
            heappush(large_list, -element)

        # Variable to keep the heaps balanced
        balance = 0

        i = k
        while True:
            # If the window size is odd
            if k % 2 == 1:
                medians.append(float(-small_list[0]))
            else:
                medians.append((-small_list[0] + large_list[0]) * 0.5)

            # Break the loop if all elements have been processed
            if i >= len(nums):
                break

            # Outgoing number
            out_num = nums[i - k]

            # Incoming number
            in_num = nums[i]
            i += 1

            # If the outgoing number is from max heap
            if out_num <= -small_list[0]:
                balance -= 1
            else:
                balance += 1

            # Add/Update the outgoing number in the hash map
            outgoing_num[out_num] = outgoing_num.get(out_num, 0) + 1

            # If the incoming number is less than the top of the max heap, add it in that heap
            # Otherwise, add it in the min heap
            if in_num <= -small_list[0]:
                balance += 1
                heappush(small_list, -in_num)
            else:
                balance -= 1
                heappush(large_list, in_num)

            # Re-balance the heaps
            if balance < 0:
                heappush(small_list, -heappop(large_list))
            elif balance > 0:
                heappush(large_list, -heappop(small_list))

            # Since the heaps have been balanced, we reset the balance variable to 0.
            balance = 0

            # Remove invalid numbers present in the hash map from top of max heap
            while (
                small_list
                and -small_list[0] in outgoing_num
                and outgoing_num[-small_list[0]] > 0
            ):
                outgoing_num[-small_list[0]] -= 1
                heappop(small_list)

            # Remove invalid numbers present in the hash map from top of min heap
            while (
                large_list
                and large_list[0] in outgoing_num
                and outgoing_num[large_list[0]] > 0
            ):
                outgoing_num[large_list[0]] -= 1
                heappop(large_list)

        return medians

from sortedcontainers import SortedList

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        window = SortedList(nums[:k])

        for i in range(k, len(nums)):
            if k % 2 == 1:
                median = window[k // 2]
            else:
                median = (window[k // 2] + window[k // 2 - 1]) / 2

            res.append(float(median))

            window.discard(nums[i - k])
            window.add(nums[i])

        # Process the last window
        if k % 2 == 1:
            median = window[k // 2]
        else:
            median = (window[k // 2] + window[k // 2 - 1]) / 2

        res.append(float(median))

        return res

    from bisect import bisect_left, insort
#Purpose of bisect_left
#The main purpose of bisect_left is to find the insertion point of a
# target element in a sorted list, maintaining the sorted order,
#or return the leftmost index where the target would be inserted if it wasn't found.

#Purpose of insort
#The main purpose of insort is to insert an element into a sorted list
#while keeping the list sorted.

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = sorted(nums[:k])
        output = []
        output.append(self.getMedian(window,k))

        for i in range(1,len(nums)-k+1):
            # remove the leftmost element from our window, by finding its pos in nums, since window is sorted.
            window.pop(bisect_left(window,nums[i-1]))
            # insert a new element by expanding 0ne position to right and insert it to its respective, position in the window maintaining the sorted order.
            insort(window,nums[i+k-1])
            # append the median your output
            output.append(self.getMedian(window,k))

        return output

    def getMedian(self,window,k):
        # any odd number & 1 evaluates to 1 and any even number & 1 evaluates to 0
        # in most programming languages 0 means False and 1 means True ,
        if k & 1:
            return window[k//2]
        return (window[k//2] + window[k//2 - 1])/2   # return sum of the two middle values divided by 2 if k is even


    # I hope everything is clear !!!


from typing import List
from collections import deque

def sliding_cost(N: int, K: int, arr: List[int]) -> None:
    # Initialize two deques to maintain smallest (lwr)
    # and largest (upr) elements
    lwr, upr = deque(), deque()

    # Initialize sums of elements in lwr and upr deques
    sum1, sum2 = 0, 0

    # Iterate through the array
    for i in range(N):
        # Remove the (i-k)th element so that window
        # contains k elements
        if i >= K:
            if arr[i - K] in lwr:
                lwr.remove(arr[i - K])
                sum1 -= arr[i - K]
            else:
                upr.remove(arr[i - K])
                sum2 -= arr[i - K]

        # Calculate sizes of lwr and upr deques
        sz1, sz2 = len(lwr), len(upr)

        # Insert the current element into the appropriate
        # deque and update the sum
        if sz1 <= sz2:
            lwr.append(arr[i])
            sum1 += arr[i]
        else:
            upr.append(arr[i])
            sum2 += arr[i]

        # Calculate sizes of lwr and upr deques
        sz1, sz2 = len(lwr), len(upr)

        # Ensure that lwr deque contains the smallest
        # elements and upr deque contains the largest
        # elements
        if sz1 > 0 and sz2 > 0:
            # Find the maximum from lwr and the minimum
            # from upr
            max_lwr = max(lwr)
            min_upr = min(upr)

            # If the maximum element from lwr is greater
            # than the minimum element from upr, swap them.
            if max_lwr > min_upr:
                sum1 = sum1 + (min_upr - max_lwr)
                sum2 = sum2 + (max_lwr - min_upr)
                lwr.remove(max_lwr)
                upr.remove(min_upr)
                lwr.append(min_upr)
                upr.append(max_lwr)

        # Output the calculated cost for the current window
        if i >= (K - 1):
            median = max(lwr)
            print((sz1 * median - sum1) + (sum2 - median * sz2), end=" ")

# Driver Code
if __name__ == "__main__":
    N, K = 8, 3

    # Input array
    arr = [2, 4, 3, 5, 8, 1, 2, 1]

    # Call the sliding_cost function
    sliding_cost(N, K, arr)

from sortedcontainers import SortedList

def sliding_median_abs_diff(n, m, a):
    st = SortedList(a[:m])  # Maintain a sorted list of the first m elements
    median_index = (m - 1) // 2  # 0-based index of median
    P = st[median_index]

    # Compute initial cost
    d = sum(abs(x - P) for x in st)
    result = [d]

    for i in range(n - m):
        st.remove(a[i])  # Remove outgoing element
        st.add(a[i + m])  # Add new incoming element

        p = st[median_index]  # Get new median
        d += abs(p - a[i + m]) - abs(P - a[i])

        if m % 2 == 0:  # Adjust for even-sized window
            d -= p - P

        P = p
        result.append(d)

    print(*result)

# Example usage
n, m = map(int, input().split())
a = list(map(int, input().split()))
sliding_median_abs_diff(n, m, a)


WIDTH = 1000

barn = [[0 for _ in range(WIDTH + 1)] for _ in range(WIDTH + 1)]
with open("paintbarn.in") as read:
    rect_num, paint_req = [int(i) for i in read.readline().split()]
    for _ in range(rect_num):
        start_x, start_y, end_x, end_y = [int(i) for i in read.readline().split()]
        # Set up the prefix sums array with all the corners of the given rectangle
        barn[start_x][start_y] += 1
        barn[start_x][end_y] -= 1
        barn[end_x][start_y] -= 1
        barn[end_x][end_y] += 1

valid_area = 0
# Run 2D prefix sums on the array
for x in range(WIDTH + 1):
    for y in range(WIDTH + 1):
        if x > 0:
            barn[x][y] += barn[x - 1][y]
        if y > 0:
            barn[x][y] += barn[x][y - 1]
        if x > 0 and y > 0:
            barn[x][y] -= barn[x - 1][y - 1]
        valid_area += barn[x][y] == paint_req

print(valid_area, file=open("paintbarn.out", "w"))

# SORTING
from functools import cmp_to_key
import sys

def compare(a, b):
    return -1 if a + b > b + a else 1

def solve():
    nums = sorted(map(lambda s: s.rstrip(), sys.stdin.readlines()[1:]), key=cmp_to_key(compare))
    print("".join(nums))

def main():
    solve()

if __name__ == "__main__":
    main()

import sys

def solve():
    t = int(sys.stdin.readline().strip())

    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        a = list(map(int, sys.stdin.readline().split()))

        a.sort(reverse=True)  # Sort in descending order

        b = []

        # Step 1: Check if pairs exist
        for i in range(n):
            if a[i * 2] != a[i * 2 + 1]:
                print("NO")
                break
            b.append(a[i * 2])
        else:  # Executes if break is not hit
            d = [0] * n

            # Step 2: Check the required differences
            for i in range(1, n):
                if b[i - 1] == b[i] or (b[i - 1] - b[i]) % (2 * (n - i)) != 0:
                    print("NO")
                    break
                d[i] = (b[i - 1] - b[i]) // (2 * (n - i))
            else:
                # Step 3: Check the final condition
                for i in range(1, n):
                    b[n - 1] -= 2 * i * d[i]

                if b[n - 1] <= 0 or b[n - 1] % (2 * n) != 0:
                    print("NO")
                else:
                    print("YES")

def main():
    solve()

if __name__ == "__main__":
    main()

import sys
from bisect import bisect_left

class Man:
    def __init__(self, h, w, idx):
        self.h = h
        self.w = w
        self.id = idx

    def __lt__(self, other):
        return (self.h, self.w, self.id) < (other.h, other.w, other.id)

class MinPair:
    def __init__(self):
        self.mn1 = (float('inf'), -1)
        self.mn2 = (float('inf'), -1)

def create_pref_mins(arr):
    pref_min = []
    cur_min = MinPair()

    for x in arr:
        if x.w < cur_min.mn1[0]:
            cur_min.mn2 = cur_min.mn1
            cur_min.mn1 = (x.w, x.id)
        else:
            cur_min.mn2 = min(cur_min.mn2, (x.w, x.id))

        pref_min.append((x.h, MinPair()))
        pref_min[-1][1].mn1 = cur_min.mn1
        pref_min[-1][1].mn2 = cur_min.mn2

    return pref_min

def find_any(mins, h, w, idx):
    pos = bisect_left(mins, (h,))
    if pos == 0:
        return -1
    pos -= 1

    mn1, mn2 = mins[pos][1].mn1, mins[pos][1].mn2
    if mn1[1] != idx:
        return mn1[1] + 1 if mn1[0] < w else -1
    return mn2[1] + 1 if mn2[0] < w else -1

def solve():
    n = int(sys.stdin.readline().strip())
    hor, ver, a = [], [], []

    for i in range(n):
        h, w = map(int, sys.stdin.readline().split())
        hor.append(Man(h, w, i))
        ver.append(Man(w, h, i))
        a.append((h, w))

    hor.sort()
    ver.sort()

    hor_mins = create_pref_mins(hor)
    ver_mins = create_pref_mins(ver)

    res = []
    for i in range(n):
        h, w = a[i]
        idx = find_any(hor_mins, h, w, i)
        if idx == -1:
            idx = find_any(ver_mins, h, w, i)
        res.append(str(idx))

    print(" ".join(res))

def main():
    tests = int(sys.stdin.readline().strip())
    for _ in range(tests):
        solve()

if __name__ == "__main__":
    main()

# Cellular network
# At first store coordinates of all towers in set towers.

# At first store coordinates of all towers in set towers.

# Then let's look through all cities. Let the current city be located in the point cur. Let it = towers.lowerbound(cur). Then if it is not equal to the end of the set we put in the variable dist the value ( * it - cur) — the distance to the nearest tower on the right for the current city. If it is not equal to the beginning of the set we need to make it –  and update dist = min(dist, cur -  * it) — the distance to the nearest tower on the left to the current city. After that we only need to update the answer: ans = max(ans, dist).

# Also this problem can be solved with help of two pointers in linear time.
import sys
import bisect

def solve():
    n, m = map(int, sys.stdin.readline().split())  # Number of cities and towers
    cities = list(map(int, sys.stdin.readline().split()))  # City coordinates
    towers = sorted(map(int, sys.stdin.readline().split()))  # Tower coordinates (sorted for binary search)

    max_dist = 0  # Maximum of the minimum distances

    for city in cities:
        idx = bisect.bisect_left(towers, city)  # Find the position of the first tower >= city
        dist = float('inf')

        if idx < m:  # Check the nearest right-side tower
            dist = towers[idx] - city

        if idx > 0:  # Check the nearest left-side tower
            dist = min(dist, city - towers[idx - 1])

        max_dist = max(max_dist, dist)  # Update max distance

    print(max_dist)

def main():
    solve()

if __name__ == "__main__":
    main()


def min_substring_length(s):
    n = len(s)
    unique_chars = set(s)  # Find all unique characters
    num_unique = len(unique_chars)  # Number of unique characters
    INF = 10**9  # A large number

    # Initialize len array with large values
    length = [INF] * n

    # Iterate through each unique character
    for c in unique_chars:
        last = -1  # Last occurrence of character c
        for i in range(n):
            if s[i] == c:
                last = i
            if last == -1:
                length[i] = INF  # No valid substring ending at i
            else:
                length[i] = max(length[i], i - last + 1)  # Update length array

    # The answer is the minimum value in length array
    return min(length)

# Read input
def main():
    s = input().strip()
    print(min_substring_length(s))

if __name__ == "__main__":
    main()

from collections import defaultdict

def min_smartness_difference(n, m, smartness):
    smartness.sort()  # Sort smartness values
    freq = defaultdict(int)  # Frequency of topic coverage
    count = 0  # Number of topics that have found a multiple
    l = 0  # Left pointer
    ans = float('inf')  # Minimum smartness difference

    def add(x):
        """Adds student x to the team and updates topic frequency."""
        nonlocal count
        for i in range(1, min(m, x) + 1):
            if x % i == 0:
                if freq[i] == 0:
                    count += 1
                freq[i] += 1

    def remove(x):
        """Removes student x from the team and updates topic frequency."""
        nonlocal count
        for i in range(1, min(m, x) + 1):
            if x % i == 0:
                freq[i] -= 1
                if freq[i] == 0:
                    count -= 1

    for r in range(n):
        add(smartness[r])  # Add student r to the team

        while count == m:  # Check if the team is proficient
            ans = min(ans, smartness[r] - smartness[l])  # Update minimum difference
            remove(smartness[l])  # Remove student at l
            l += 1  # Move left pointer forward

    return ans if ans != float('inf') else -1  # Return minimum difference or -1 if not possible

# Read input
def main():
    n, m = map(int, input().split())
    smartness = list(map(int, input().split()))
    print(min_smartness_difference(n, m, smartness))

if __name__ == "__main__":
    main()
# Longest K-good Segment
import sys
from collections import defaultdict

def solve(n, k, a):
    freq = defaultdict(int)
    l = 0
    distinct = 0
    max_len = 0
    best_l, best_r = 0, 0

    for r in range(n):
        # Add the rightmost element
        if freq[a[r]] == 0:
            distinct += 1
        freq[a[r]] += 1

        # If we exceed k distinct values, move the left pointer
        while distinct > k:
            freq[a[l]] -= 1
            if freq[a[l]] == 0:
                distinct -= 1
            l += 1

        # Update the best segment
        if r - l + 1 > max_len:
            max_len = r - l + 1
            best_l, best_r = l + 1, r + 1  # Convert to 1-based indexing

    print(best_l, best_r)

def main():
    # Fast input reading
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    solve(n, k, a)

if __name__ == "__main__":
    main()

# LOngest Strike
import sys
from collections import Counter

def solve():
    # Read input values
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    # Count occurrences of each number
    freq = Counter(a)

    # Extract numbers that appear at least k times
    valid_numbers = [num for num, count in freq.items() if count >= k]

    if not valid_numbers:
        print(-1)
        return

    # Sort valid numbers
    valid_numbers.sort()

    # Find the longest consecutive segment
    max_length = 0
    best_l, best_r = valid_numbers[0], valid_numbers[0]
    l = valid_numbers[0]

    for i in range(1, len(valid_numbers)):
        if valid_numbers[i] - 1 == valid_numbers[i - 1]:  # Consecutive check
            if valid_numbers[i] - l > max_length:
                best_l, best_r = l, valid_numbers[i]
                max_length = valid_numbers[i] - l
        else:
            l = valid_numbers[i]  # Reset left boundary

    print(best_l, best_r)

def main():
    # Read number of test cases
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
