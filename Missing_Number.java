import java.util.*;

public class Missing_Number {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n - 1];
        for (int i = 0; i < n - 1; i++) {
            arr[i] = sc.nextInt();
        }
        System.out.println(missingNumber(arr, n));

    }

    private static int missingNumber(int[] nums, int n) {
        int len = nums.length;

        int xor1 = 0;
        int xor2 = 0;
        for (int i = 0; i < len; ++i) {
            xor1 = xor1 ^ nums[i];
            xor2 = xor2 ^ (i + 1);
        }
        xor1 = xor1 ^ n;
        return (xor1 ^ xor2);
    }
}