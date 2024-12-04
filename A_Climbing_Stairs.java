
public class A_Climbing_Stairs {
    static int climbStairs(int n) {
        int[] memo = new int[n + 1];
        if (n <= 2) {
            memo[n] = n;
            return n;
        } 
        if (memo[n - 2] == 0) {
            memo[n - 2] = climbStairs(n - 2);
        }
        if (memo[n - 1] == 0) {
            memo[n - 1] = climbStairs(n - 1);
        }
        return memo[n - 2] + memo[n - 1];
    }
    public static void main(String[] args) {
        int n = 20;
        System.out.println(climbStairs(n)); //! Output: 10946
    }
}
