from typing import List
# from sortedcontainers import SortedList
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*len(nums)

        # first left multiplication
        leftProduct =  1
        for i in range(n):
            answer[i] = leftProduct
            leftProduct *= nums[i]
        # then right multiplication along updating the answer    
        rightProduct = 1
        for i in range(n - 1,-1,-1):
            answer[i] *= rightProduct
            rightProduct = rightProduct * nums[i]


        return answer       
def even_index_prefix_sum(A: List[int]) -> List[int]:
    """Constructs an even index prefix sum array.
    
    Args:
        A (List[int]): The input array of integers.
    
    Returns:
        List[int]: The prefix sum array where each element at an even index 
                    contains the sum of all previous even indexed elements.
    """
    result = [0] * len(A)  # Initialize the result array
    prefix_sum = 0  # Variable to hold the current prefix sum

    for i in range(len(A)):
        if i % 2 == 0:  # Check if the index is even
            prefix_sum += A[i]  # Add the current element to the prefix sum
        result[i] = prefix_sum  # Assign the prefix sum to the result array

    return result


def odd_index_prefix_sum(A: List[int]) -> List[int]:
    """Constructs an odd index prefix sum array.
    
    Args:
        A (List[int]): The input array of integers.
    
    Returns:
        List[int]: The prefix sum array where each element at an odd index 
                    contains the sum of all previous odd indexed elements.
    """
    result = [0] * len(A)  # Initialize the result array
    prefix_sum = 0  # Variable to hold the current prefix sum

    for i in range(len(A)):
        if i % 2 != 0:  # Check if the index is odd
            prefix_sum += A[i]  # Add the current element to the prefix sum
        result[i] = prefix_sum  # Assign the prefix sum to the result array

    return result
class Solution1413:
    """1413. Minimum Value to Get Positive Step by Step Sum
    
    This class contains a method to determine the minimum starting value
    required to ensure the cumulative sum at any point is positive.
    """
    def minStartValue(self, nums: List[int]) -> int:
        """Calculates the minimum starting value.
        
        Args:
            nums (List[int]): The list of integers.
        
        Returns:
            int: The minimum start value.
        """
        sum_value = 0
        min_prefix_sum = float('inf')
        
        for num in nums:
            sum_value += num
            min_prefix_sum = min(min_prefix_sum, sum_value)
        
        return 1 if min_prefix_sum >= 0 else -min_prefix_sum + 1


class Solution548:
    """548. Split Array with Equal Sum
    
    This class checks if it is possible to split the array into four
    non-empty parts with equal sums.
    """
    def splitArray(self, nums: List[int]) -> bool:
        """Determines if the array can be split into four equal sum parts.
        
        Args:
            nums (List[int]): The list of integers.
        
        Returns:
            bool: True if the array can be split, False otherwise.
        """
        n = len(nums)
        prefix = [0] * (n + 1)
        sum_set = set()
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        for j in range(3, n - 2):
            for i in range(0, j - 1):
                sum1 = prefix[i + 1]
                sum2 = prefix[j] - prefix[i + 1]
                if sum1 == sum2:
                    sum_set.add(sum1)
            
            for k in range(j + 2, n - 1):
                sum3 = prefix[k] - prefix[j + 1]
                sum4 = prefix[n] - prefix[k + 1]
                if sum3 in sum_set and sum3 == sum4:
                    return True

        return False


def getPrefixSum(matrix: List[List[int]]) -> List[List[int]]:
    """Calculates the prefix sum of a 2D matrix.
    
    Args:
        matrix (List[List[int]]): The 2D matrix of integers.
    
    Returns:
        List[List[int]]: The prefix sum matrix.
    """
    m = len(matrix)
    n = len(matrix[0])
    prefix = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            prefix[i][j] = (prefix[i][j - 1] + prefix[i - 1][j] -
                            prefix[i - 1][j - 1] + matrix[i - 1][j - 1])
    
    return prefix


def rangeSum(prefix: List[List[int]], row1: int, col1: int, row2: int, col2: int) -> int:
    """Calculates the sum of elements in a submatrix defined by (row1, col1) to (row2, col2).
    
    Args:
        prefix (List[List[int]]): The prefix sum matrix.
        row1 (int): The starting row index.
        col1 (int): The starting column index.
        row2 (int): The ending row index.
        col2 (int): The ending column index.
    
    Returns:
        int: The sum of the submatrix.
    """
    return (prefix[row2 + 1][col2 + 1] - prefix[row1][col2 + 1] -
            prefix[row2 + 1][col1] + prefix[row1][col1])


class Solution1074:
    """1074. Number of Submatrices That Sum to Target
    
    This class counts the number of submatrices that sum to a given target.
    """
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        """Counts the number of submatrices that sum to the target.
        
        Args:
            matrix (List[List[int]]): The 2D matrix of integers.
            target (int): The target sum.
        
        Returns:
            int: The number of submatrices that sum to the target.
        """
        m = len(matrix)
        n = len(matrix[0])
        prefix = getPrefixSum(matrix)
        ans = 0
        
        for r1 in range(m):
            for r2 in range(r1, m):
                count = {}
                for c in range(n):
                    total = rangeSum(prefix, r1, c, r2, c)
                    if total == target:
                        ans += 1
                    count[total] = count.get(total, 0) + 1
                    ans += count.get(total - target, 0)

        return ans


class Solution363:
    """363. Max Sum of Rectangle No Larger Than K
    
    This class finds the maximum sum of a rectangle no larger than a given value k.
    """
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        """Finds the maximum sum of a rectangle no larger than k.
        
        Args:
            matrix (List[List[int]]): The 2D matrix of integers.
            k (int): The maximum allowed sum.
        
        Returns:
            int: The maximum sum of a rectangle no larger than k.
        """
        m = len(matrix)
        n = len(matrix[0])
        max_sum = float('-inf')

        for r1 in range(m):
            row_sum = [0] * n
            for r2 in range(r1, m):
                for c in range(n):
                    row_sum[c] += matrix[r2][c]

                sorted_list = sorted([0]) # SOrtedList
                curr_sum = 0
                for sum_val in row_sum:
                    curr_sum += sum_val
                    idx = sorted_list.bisect_left(curr_sum - k)
                    if idx < len(sorted_list):
                        max_sum = max(max_sum, curr_sum - sorted_list[idx])
                    sorted_list.add(curr_sum)

        return max_sum


class Solution525:
    """525. Contiguous Array
    
    This class finds the maximum length of a contiguous subarray with an equal number of 0 and 1.
    """
    def findMaxLength(self, nums: List[int]) -> int:
        """Finds the maximum length of a contiguous subarray with equal number of 0s and 1s.
        
        Args:
            nums (List[int]): The binary array (0s and 1s).
        
        Returns:
            int: The maximum length of the contiguous subarray.
        """
        count_map = {0: -1}
        max_length = 0
        count = 0

        for i in range(len(nums)):
            count += 1 if nums[i] == 1 else -1
            if count in count_map:
                max_length = max(max_length, i - count_map[count])
            else:
                count_map[count] = i

        return max_length


if __name__ == "__main__":
    # Example usage for each solution class

    # Example for Solution1413
    sol1413 = Solution1413()
    print(sol1413.minStartValue([-3, 2, -3, 4, 2]))  # Output: 5

    # Example for Solution548
    sol548 = Solution548()
    print(sol548.splitArray([1, 2, 1, 2, 1, 2, 1]))  # Output: True

    # Example for Solution1074
    sol1074 = Solution1074()
    print(sol1074.numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0))  # Output: 4

    # Example for Solution363
    sol363 = Solution363()
    print(sol363.maxSumSubmatrix([[1, 0, 1], [0, -2, 3], [1, 1, 1]], 2))  # Output: 3

    # Example for Solution525
    sol525 = Solution525()
    print(sol525.findMaxLength([0, 1]))  # Output: 2
