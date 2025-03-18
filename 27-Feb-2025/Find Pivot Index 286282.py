# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/

class Solution:  
    def pivotIndex(self, arr):  
        n = len(arr)  # Get the length of the array  

        # Handle the case for an empty array  
        if n == 0:  
            return -1  

        net = sum(arr)  # Calculate the total sum of the array  

        left = 0  
        right = net  # Initialize right with the total sum  

        # Iterate through the array to find the equilibrium index  
        for i in range(n):  
            right -= arr[i]  # Update right for current index  

            # Check if left sum equals right sum  
            if left == right:  
                return i  # Returning the equilibrium index  

            left += arr[i]  # Update left for the next iteration  

        return -1  # Return -1 if no equilibrium index is found