import java.util.*;

public class A_X_Axis {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt(); // Number of test cases
        while (t-- > 0) {
            int[] arr = new int[3];
            for (int i = 0; i < 3; i++) { // x1,x2,x3
                arr[i] = sc.nextInt();
            }
            System.out.println(findSmallest(arr));
        }
    }

    private static int findSmallest(int[] nums) {
        int n = nums.length;
        int minDis = Integer.MAX_VALUE;

        for (int i = 0; i < n; i++) {
            int currentdis = 0;
            int left = i - 1;
            while (left >= 0) {
                currentdis += Math.abs(nums[left] - nums[i]);
                left--;
            }
            int right = i + 1;
            while (right < n) {
                currentdis += Math.abs(nums[right] - nums[i]);
                right++;
            }
            minDis = Math.min(minDis, currentdis);
        }

        return minDis;
    }
}
