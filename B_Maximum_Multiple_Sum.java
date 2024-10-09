import java.util.*;

public class B_Maximum_Multiple_Sum {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int t = scanner.nextInt();
        for (int i = 0; i < t; i++) {
            int n = scanner.nextInt();
            int optimalX = 2; // Starting from the minimum x value
            long maxSum = 0; // To keep track of the maximum sum
            for (int x = 2; x <= n; x++) {
                int k = n / x; // Find k such that kx <= n
                // Calculate the sum of multiples of x
                long sum = x * (k * (k + 1)) / 2; // Use long to avoid overflow

                // Check if this sum is greater than the max found so far
                if (sum > maxSum) {
                    maxSum = sum; // Update max sum
                    optimalX = x; // Update optimal x
                }
            }
            System.out.println(optimalX); // Output the optimal x for this test case
        }
        scanner.close(); // Closing the scanner
    }
}