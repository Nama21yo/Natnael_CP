
public class G_Knight_Cursed {
    static int cursed(int n) {
        int[] memo = new int[n + 1];
        
        if(n <= 2) {
            memo[n] = n;
            return n;
        }
        if (memo[n - 3] == 0) {
            return cursed(n - 3); //it is cursed don't try it
        }
        if (memo[n - 2] == 0) {
            memo[n - 2] = cursed(n - 2);
        }
        if (memo[n - 1] == 0) {
            memo[n - 1] = cursed(n - 1);
        }
        return memo[n - 3] + memo[n - 2] + memo[n - 1];
    }
    public static void main(String[] args) {
        int steps = 30;
        System.out.println(cursed(steps)); // Output - 0
    }
}

