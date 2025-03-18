from collections import deque

def increasing_monotonic_queue(arr, n):
	q = deque()
	for i in range(n):
		while len(q) > 0 and q[-1] > arr[i]:
			q.pop()
		q.append(arr[i])
	return q

arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
q = increasing_monotonic_queue(arr, n)
for i in q:
	print(i, end=' ')

# Function to calculate Decreasing
# Monotonic queue
def decreasing_monotonic_queue(arr):
	n = len(arr)
	q = deque()
	for i in range(n):

		# If recently added element is
		# smaller than current element
		while q and q[-1] < arr[i]:

			q.pop()

		q.append(arr[i])

	return q

# Driver Code
arr = [6, 5, 4, 3, 2, 1]

# Function call
q = decreasing_monotonic_queue(arr)

for i in q:
	print(i)
def sumSubarrayMins(A):
    n = len(A)
    left = [0] * n  # List to store the maximum length of the subarray on the left side
    right = [0] * n  # List to store the maximum length of the subarray on the right side
    
    # Initialize left[i] = i + 1 (each element is at least in its own subarray)
    # Initialize right[i] = n - i (each element can extend up to the end of the array)
    for i in range(n):
        left[i] = i + 1
        right[i] = n - i

    # Stack to store the indices of elements
    stack = []
    
    # Iterate through the array to compute the previous less element (left) and next less element (right)
    for i in range(n):
        # When we find an element smaller than the top of the stack, we calculate the right limits
        while stack and A[i] < A[stack[-1]]:
            tp = stack.pop()  # Pop the element and update the right boundary
            right[tp] = i - tp  # The next smaller element for tp is A[i]
        
        # If stack is not empty, set the left boundary
        if stack:
            left[i] = i - stack[-1]  # Previous less element for A[i]
        
        # Push the current index onto the stack
        stack.append(i)
    
    # Calculate the answer using the left and right boundaries and elements of A
    ans = 0
    mod = 1_000_000_007  # Modulo value
    for i in range(n):
        ans += (long(left[i]) * long(right[i]) * A[i]) % mod
        ans %= mod  # Keep the result within bounds of modulo
    
    return ans

# Example usage:
A = [3, 1, 2, 4]
print(sumSubarrayMins(A))  # Output the result


class MonotonicQueue:
    def __init__(self):
        self.maxq = []
    
    def push(self, n):
        # remove all elements less than n
        while self.maxq and self.maxq[-1] < n: 
            self.maxq.pop()
        # then add n to the end
        self.maxq.append(n)
    
    def max(self):
        return self.maxq[0]
    
    def pop(self, n):
        if n == self.maxq[0]:
            self.maxq.pop(0)

class Solution(object):
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MonotonicQueue()
        res = []
        
        for i in range(len(nums)):
            if i < k - 1:
                # first fill the window with the first k - 1 elements
                window.push(nums[i])
            else: 
                # slide the window forward, add new number
                window.push(nums[i])
                # record the maximum value of the current window
                res.append(window.max())
                # remove the old number
                window.pop(nums[i - k + 1])
        return res
# Circular Array
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        # Use an array to simulate a stack
        s = []
        # Double the array length to simulate a circular array
        for i in range(2 * n - 1, -1, -1):
            # Index i needs to be modulo, the rest is the same as the template
            while s and s[-1] <= nums[i % n]:
                s.pop()
            res[i % n] = -1 if not s else s[-1]
            s.append(nums[i % n])
        return res

# Queue Sort
def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    fm = 0
    for i in range(n):
        if a[i] < a[fm]:
            fm = i
    for i in range(fm + 1, n):
        if a[i] < a[i - 1]:
            print(-1)
            return
    print(fm)
 
 
for _ in range(int(input())):
    solve()
class Solution:
    def shortestSubarray(self, nums: List[int], target_sum: int) -> int:
        n = len(nums)

        # Size is n+1 to handle subarrays starting from index 0
        prefix_sums = [0] * (n + 1)

        # Calculate prefix sums
        for i in range(1, n + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

        candidate_indices = deque()

        shortest_subarray_length = float("inf")

        for i in range(n + 1):
            # Remove candidates from front of deque where subarray sum meets target
            while (
                candidate_indices
                and prefix_sums[i] - prefix_sums[candidate_indices[0]]
                >= target_sum
            ):
                # Update shortest subarray length
                shortest_subarray_length = min(
                    shortest_subarray_length, i - candidate_indices.popleft()
                )

            # Maintain monotonicity by removing indices with larger prefix sums
            while (
                candidate_indices
                and prefix_sums[i] <= prefix_sums[candidate_indices[-1]]
            ):
                candidate_indices.pop()

            # Add current index to candidates
            candidate_indices.append(i)

        # Return -1 if no valid subarray found
        return (
            shortest_subarray_length
            if shortest_subarray_length != float("inf")
            else -1
        )