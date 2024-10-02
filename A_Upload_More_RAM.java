import java.util.*;

public class A_Upload_More_RAM {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt(); // Number of test cases
        while (t-- > 0) {
            int n = sc.nextInt();
            int k = sc.nextInt();
            if (k == 1) {
                System.out.println(n);
            } else {
                // 5 1
                // 1 1 1 1 1 = 5

                // 2 2
                // 10 1 = (n - 1) * k + 1 = 3

                // 2 3
                // 100 1 = (n - 1) * k + 1 = 4

                // 1 7
                // 1 = (n - 1) * k + 1 = 1

                System.out.println((n - 1) * k + 1);
            }
        }
    }
}
